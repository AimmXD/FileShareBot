from pyrogram import Client, filters
from pyrogram.types import Message
from utils import ButtonManager
import config

button_manager = ButtonManager()

@Client.on_message(filters.command("about"))
async def about_command(client: Client, message: Message):
    about_text = config.Messages.ABOUT_TEXT.format(
        bot_name=config.BOT_NAME,
        version=config.BOT_VERSION
    )
    await message.reply_text(about_text, reply_markup=button_manager.about_button())
