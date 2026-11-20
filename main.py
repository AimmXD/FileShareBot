#ProBotts bot join @ZeoXpro
from pyrogram import Client, idle
from web import start_webserver, ping_server
from database import Database
import config
import asyncio
import os
import time


class FileShareBot(Client):
    def __init__(self):
        super().__init__(
            name="FileShareBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            plugins=dict(root="handlers")
        )
        self.db = Database()
        print("Bot Initialized!")

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"Bot Started as {me.first_name}")
        print(f"Username: @{me.username}")
        print("----------------")

       

    async def stop(self):
        await super().stop()
        print("Bot Stopped. Bye!")

async def main():
    bot = FileShareBot()
    
    try:
        print("Starting Bot...")
        await bot.start()
        print("Bot is Running!")
        if config.WEB_SERVER:
            asyncio.create_task(start_webserver())
            asyncio.create_task(ping_server(config.PING_URL, config.PING_TIME))
            
        await idle()
    except Exception as e:
        print(f"ERROR: {str(e)}")
    finally:
        await bot.stop()
        print("Bot Stopped!")


if __name__ == "__main__":
    try:
        
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Bot Stopped by User!")
    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
