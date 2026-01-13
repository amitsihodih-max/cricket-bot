import asyncio
from telegram import Bot
from post_prediction import get_prediction

BOT_TOKEN = "8591884031:AAGFIxdI5rLsq_qlLBemgO9O1rNbLyHuxIk"
CHANNEL_ID = "-1003263006563"

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    text = get_prediction()
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=text
    )

async def main():
    while True:
        await send_message()
        await asyncio.sleep(10800)  # 3 hours

asyncio.run(main())
