from pyrogram import Client
import asyncio
import logging

logger = logging.getLogger(__name__)

async def schedule_message_deletion(client: Client, file_uuid: str, chat_id: int, message_ids: list, delete_time: int):
    await asyncio.sleep(delete_time * 60)
    try:
        await client.delete_messages(chat_id, message_ids)
        notification_msg = await client.send_message(
            chat_id=chat_id,
            text=(
                "🕒 **Auto-Delete Notification**\n\n"
                "The file you received has been automatically deleted.\n\n"
                "• You can request the file again using the same link\n"
                "• Save important files to your saved messages\n"
                "• Auto-delete helps maintain server space\n\n"
                "💡 The file remains in our database for future access"
            )
        )
        await asyncio.sleep(30)
        await notification_msg.delete()
    except Exception as e:
        logger.error(f"Error in message deletion: {str(e)}")
