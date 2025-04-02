import os
import asyncio
import yt_dlp
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils.executor import start_polling

# === তোমার টেলিগ্রাম বটের টোকেন ===
BOT_TOKEN = "7551049610:AAG2cCdhEjKU8RSn_qgP87urZr1C4AYEzWk"

# === বট ইনিশিয়ালাইজ করা ===
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def download_video(url):
    """ ভিডিও ডাউনলোড করার ফাংশন """
    output_file = "downloaded_video.mp4"
    ydl_opts = {
        'outtmpl': output_file,
        'format': 'bestvideo+bestaudio/best',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return output_file

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    """ ইউজার যখন /start কমান্ড পাঠাবে """
    await message.reply("👋 স্বাগতম! শুধু ভিডিওর লিংক পাঠান, আমি ডাউনলোড করে দিবো!")

@dp.message_handler()
async def handle_video_download(message: types.Message):
    """ ইউজার লিংক পাঠালে ভিডিও ডাউনলোড করে পাঠাবে """
    url = message.text.strip()
    if any(x in url for x in ["youtube.com", "youtu.be", "facebook.com", "instagram.com", "tiktok.com", "terabox.com"]):
        try:
            await message.reply("⏳ ভিডিও ডাউনলোড করা হচ্ছে...")
            video_path = await download_video(url)
            await bot.send_video(message.chat.id, InputFile(video_path))
            os.remove(video_path)  # ভিডিও পাঠানোর পর ডিলিট করা
        except Exception as e:
            await message.reply(f"❌ ভিডিও ডাউনলোড করতে সমস্যা হয়েছে: {e}")
    else:
        await message.reply("❌ সঠিক ভিডিও লিংক পাঠান!")

if name == "main":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
