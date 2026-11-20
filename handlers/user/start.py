from pyrogram import Client, filters
from pyrogram.types import Message
from database import Database
from utils import ButtonManager
import config
import asyncio
import logging
from ..utils.message_delete import schedule_message_deletion

logger = logging.getLogger(__name__)
db = Database()
button_manager = ButtonManager()

@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await db.add_user(message.from_user.id, message.from_user.username)
    
    if len(message.command) > 1:
        command = message.command[1]
        file_uuid = message.command[1]
        
        force_sub_status = await button_manager.check_force_sub(client, message.from_user.id)
        if not force_sub_status:
            force_sub_text = "**⚠️ You must join our channel(s) to use this bot!**\n\n"
            
            if config.FORCE_SUB_CHANNEL != 0:
                force_sub_text += "• Join Channel 1\n"
            if config.FORCE_SUB_CHANNEL_2 != 0:
                force_sub_text += "• Join Channel 2\n"
                
            force_sub_text += "\nJoin the channel(s) and try again."
            
            await message.reply_text(
                force_sub_text,
                reply_markup=button_manager.force_sub_button(file_uuid),
                protect_content=config.PRIVACY_MODE
            )
            return

        if command.startswith("batch_"):
            batch_uuid = command.replace("batch_", "")
            batch_data = await db.get_batch(batch_uuid)
            
            if not batch_data:
                await message.reply_text(
                    "❌ Batch not found or has been deleted!", 
                    protect_content=config.PRIVACY_MODE
                )
                return
            
            status_msg = await message.reply_text(
                f"🔄 **Processing Batch Download**\n\n"
                f"📦 Total Files: {len(batch_data['files'])}\n"
                f"⏳ Please wait...",
                protect_content=config.PRIVACY_MODE
            )
            
            success_count = 0
            failed_count = 0
            sent_msgs = []
            
            for file_uuid in batch_data["files"]:
                file_data = await db.get_file(file_uuid)
                if file_data and "message_id" in file_data:
                    try:
                        msg = await client.copy_message(
                            chat_id=message.chat.id,
                            from_chat_id=config.DB_CHANNEL_ID,
                            message_id=file_data["message_id"],
                            protect_content=config.PRIVACY_MODE
                        )
                        if msg and msg.id:
                            sent_msgs.append(msg.id)
                            success_count += 1
                            
                            if file_data.get("auto_delete"):
                                delete_time = file_data.get("auto_delete_time", getattr(config, 'DEFAULT_AUTO_DELETE', 30))
                                info_msg = await msg.reply_text(
                                    f"⏳ **File Auto-Delete Information**\n\n"
                                    f"This file will be automatically deleted in {delete_time} minutes\n"
                                    f"• Delete Time: {delete_time} minutes\n"
                                    f"• Time Left: {delete_time} minutes\n"
                                    f"💡 **Save this file to your saved messages before it's deleted!**",
                                    protect_content=config.PRIVACY_MODE
                                )
                                if info_msg and info_msg.id:
                                    sent_msgs.append(info_msg.id)
                                    asyncio.create_task(schedule_message_deletion(
                                        client, file_uuid, message.chat.id, [msg.id, info_msg.id], delete_time
                                    ))
                    except Exception as e:
                        failed_count += 1
                        logger.error(f"Batch file send error: {str(e)}")
                        continue
            
            if success_count > 0:
                await db.increment_batch_downloads(batch_uuid)
            
            status_text = (
                f"✅ **Batch Download Complete**\n\n"
                f"📥 Successfully sent: {success_count} files\n"
                f"❌ Failed: {failed_count} files"
            )
            await status_msg.edit_text(status_text)
            
        else:
            file_uuid = command
            file_data = await db.get_file(file_uuid)
            
            if not file_data:
                await message.reply_text(
                    "❌ File not found or has been deleted!", 
                    protect_content=config.PRIVACY_MODE
                )
                return
            
            try:
                msg = await client.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=config.DB_CHANNEL_ID,
                    message_id=file_data["message_id"],
                    protect_content=config.PRIVACY_MODE
                )
                
                if msg and msg.id:
                    await db.increment_downloads(file_uuid)
                    
                    if file_data.get("auto_delete"):
                        delete_time = file_data.get("auto_delete_time", getattr(config, 'DEFAULT_AUTO_DELETE', 30))
                        info_msg = await msg.reply_text(
                            f"⏳ **File Auto-Delete Information**\n\n"
                            f"This file will be automatically deleted in {delete_time} minutes\n"
                            f"• Delete Time: {delete_time} minutes\n"
                            f"• Time Left: {delete_time} minutes\n"
                            f"💡 **Save this file to your saved messages before it's deleted!**",
                            protect_content=config.PRIVACY_MODE
                        )
                        
                        if info_msg and info_msg.id:
                            asyncio.create_task(schedule_message_deletion(
                                client, file_uuid, message.chat.id, [msg.id, info_msg.id], delete_time
                            ))
                    
            except Exception as e:
                await message.reply_text(
                    f"❌ Error: {str(e)}", 
                    protect_content=config.PRIVACY_MODE
                )
                
    else:
        await message.reply_text(
            config.Messages.START_TEXT.format(
                bot_name=config.BOT_NAME,
                user_mention=message.from_user.mention
            ),
            reply_markup=button_manager.start_button(),
            protect_content=config.PRIVACY_MODE
        )
