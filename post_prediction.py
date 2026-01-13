import asyncio
from telegram import Bot

# ======================
# SETTINGS
# ======================
BOT_TOKEN = "8591884031:AAGFIxdI5rLsq_qlLBemgO9O1rNbLyHuxIk"
CHANNEL_ID = "-1003263006563"
TEST_MODE = True

bot = Bot(token=BOT_TOKEN)

async def main():
    if TEST_MODE:
        message = (
            "🏏 TEST PREDICTION\n\n"
            "Match: India 🇮🇳 vs Australia 🇦🇺\n"
            "Prediction: India will win ✅\n"
            "Confidence: 65%\n\n"
            "🤖 Bot is working perfectly!"
        )

        await bot.send_message(chat_id=CHANNEL_ID, text=message)
        print("✅ Test message sent successfully")

if __name__ == "__main__":
    asyncio.run(main())
import time

print("Bot started and running forever")

while True:
    time.sleep(60)
