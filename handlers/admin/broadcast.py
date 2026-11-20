from pyrogram import Client, filters
from pyrogram.types import Message
from database import Database
from utils import is_admin
import asyncio

db = Database()

@Client.on_message(filters.command("broadcast"))
async def broadcast_command(client: Client, message: Message):
    if not is_admin(message):
        return await message.reply_text("⚠️ You’re not allowed to use this command, darling!")

    users = await db.get_all_users()
    success, failed = 0, 0

    text = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    replied = message.reply_to_message

    if not replied and not text:
        return await message.reply_text("💌 Please either reply to a message or provide some text to broadcast, my love~")

    status_msg = await message.reply("📢 Starting broadcast...")

    for user in users:
        try:
            user_id = int(user["user_id"])

            if replied:
                await replied.forward(chat_id=user_id)
            elif text:
                await client.send_message(chat_id=user_id, text=text)

            success += 1
        except Exception as e:
            print(f"Failed to send to {user_id}: {e}")
            failed += 1
        await asyncio.sleep(0.3)

    await status_msg.edit_text(
        f"✅ **Broadcast Completed**\n\n"
        f"🎯 Success: {success}\n"
        f"❌ Failed: {failed}\n"
        f"📦 Total: {success + failed}"
    )
