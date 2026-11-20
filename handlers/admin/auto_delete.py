from pyrogram import Client, filters
from pyrogram.types import Message
from utils import is_admin
import config

@Client.on_message(filters.command("auto_del"))
async def auto_delete_command(client: Client, message: Message):
    if not is_admin(message):
        await message.reply_text("⚠️ You are not authorized to use this command!")
        return
    
    if len(message.command) != 2:
        await message.reply_text(
            "**📝 Auto Delete Command Usage**\n\n"
            "`/auto_del <minutes>`\n\n"
            "**Examples:**\n"
            "• `/auto_del 5` - Set auto-delete to 5 minutes\n"
            "• `/auto_del 60` - Set auto-delete to 1 hour\n"
            "• `/auto_del 1440` - Set auto-delete to 24 hours\n\n"
            "**Note:** Time must be between 1 and 10080 minutes (7 days)"
        )
        return
    
    try:
        delete_time = int(message.command[1])
        if not 1 <= delete_time <= 10080:
            await message.reply_text(
                "❌ **Invalid Time Range**\n\n"
                "Time must be between 1 and 10080 minutes (7 days)\n"
                "Examples:\n"
                "• 5 = 5 minutes\n"
                "• 60 = 1 hour\n"
                "• 1440 = 24 hours"
            )
            return
        
        config.DEFAULT_AUTO_DELETE = delete_time
        await message.reply_text(
            f"✅ **Auto-delete time updated**\n\n"
            f"New files will be automatically deleted after {delete_time} minutes\n"
            f"Time in other units:\n"
            f"• Hours: {delete_time/60:.1f}\n"
            f"• Days: {delete_time/1440:.1f}"
        )
    except ValueError:
        await message.reply_text(
            "❌ **Invalid Time Format**\n\n"
            "Please provide a valid number of minutes\n"
            "Example: `/auto_del 30` for 30 minutes"
        )
