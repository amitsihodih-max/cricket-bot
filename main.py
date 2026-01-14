import asyncio
import os
from telegram import Bot
from post_prediction import send_prediction

BOT_TOKEN = os.getenv("8591884031:AAGFIxdI5rLsq_qlLBemgO9O1rNbLyHuxIk")
CHANNEL_ID = os.getenv("-1003263006563")


async def send_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text="🤖 Cloud bot is alive!"
    )


async def main():
    await send_message()
    await send_prediction()   # send cricket prediction once


if __name__ == "__main__":
    asyncio.run(main())
