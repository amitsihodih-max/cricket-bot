import asyncio
from telegram import Bot

BOT_TOKEN = "8591884031:AAGFIxdI5rLsq_qlLBemgO9O1rNbLyHuxIk"
CHANNEL_ID = "-1003263006563"

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text="🤖 Cloud bot is alive!"
    )

async def main():
    while True:
        await send_message()
        await asyncio.sleep(3600)  # 1 hour

if __name__ == "__main__":
    asyncio.run(main())
