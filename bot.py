from telegram import Bot
import asyncio
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import timezone

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = "@philsaf18"

MESSAGE = """
✨ 𝑵𝒆𝒘 𝑾𝒆𝒆𝒌, 𝑺𝒂𝒎𝒆 𝑮𝒐𝒂𝒍𝒔 ✨

Staying locked in 🎯 with the same vision and focus of becoming a successful trader 📈💼

💡 Dropping top trade ideas for the week… stay tuned 👀🔥
"""


async def send_message():
    bot = Bot(token=TOKEN)

    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=MESSAGE
    )

    print("Weekly message sent successfully")


async def main():
    scheduler = AsyncIOScheduler(timezone=timezone.utc)

    scheduler.add_job(
        send_message,
        trigger="cron",
        day_of_week="sun",
        hour=17,
        minute=0
    )

    scheduler.start()

    print("Telegram bot scheduler is running...")

    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())