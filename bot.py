from loader import dp,bot,db,ADMINS
from aiogram import Bot,Dispatcher,types
from aiogram import F
from aiogram.types import Message,FSInputFile,InputMediaPhoto,InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import CommandStart
import asyncio
import handlers
import os
import logging
import sys
import handlers
from menucommands.set_bot_commands  import set_default_commands
from insta import insta_save
from tiktok import tiktok_save
from youtube import youtube_save
from pinterest import pinterest_save
# from throttling import ThrottlingMiddleware
# from admin_keyboard import admin_button


# @dp.message(F.text.contains("youtub"))
# async def yutube_download(message: types.Message):
#     video_url = youtube_save(message.text)
    
#     if video_url:
#         file_name = 'video.mp4'
#         downloaded_file = download_video(video_url, file_name)
        
#         if downloaded_file:
#             video = FSInputFile(downloaded_file)
#             await message.answer_video(video=video, caption="@BoburrrrrrrrrrrrrrrrrrrrrrBot")
#             os.remove(downloaded_file)  # Faylni yuborganingizdan so'ng o'chirish
#         else:
#             await message.answer("Video yuklab olishda xato yuz berdi.")
#     else:
#         await message.answer("Video topilmadi yoki URL noto'g'ri.")
#     # await message.answer("siz yutube link yubordingiz")

@dp.message(F.text.contains("yout"))
async def video_yuklash(message: Message):
    link = message.text
    try:
        loading_message = await message.answer("Video yuklanmoqda...✍️💬")
        yuklangan_video = youtube_save(link)
        await loading_message.delete()
        await message.answer_video(video=yuklangan_video)
    except Exception as e:
        await message.reply("Uzr, havolani yuklab olishda xatolik yuz berdi.")


@dp.message(F.text.contains("instagram"))
async def instagram_download(message:Message):
    link = message.text
    loading_message = await message.answer("Ma'lumot yuklanmoqda...✍️💬")
    instagram = insta_save(link)
    await loading_message.delete()
    video=instagram.get("video")
    rasmlar=instagram.get("images")
    if rasmlar:
        rasm=[]
        for i,r in enumerate(rasmlar):
            rasm.append(InputMediaPhoto(media=r))
            if (i+1)%10==0:
                await message.answer_media_group(rasm)
                rasm=[]
        if rasm:
            await message.answer_media_group(rasm)
    if video:
        await message.answer_video(video=video)


# @dp.message(F.text.contains("instagram"))
# async def instagram_download(message:Message):
#     try:
#         link = message.get_args()
#         if not link:
#             await message.answer("Iltimos, URL manzilni kiriting.")
#             return

#         media = insta_save(link)
        
#         if "error" in media:
#             await message.answer(media["error"])
#         elif "images" in media:
#             for img_url in media["images"]:
#                 await message.answer_photo(img_url)
#         elif "video" in media:
#             await message.answer_video(media["video"])
#     except Exception as e:
#         await message.answer(f"Xato yuz berdi: {str(e)}")

@dp.message(F.text.contains("tiktok"))
async def tiktok_download(message: Message):
    link = message.text
    loading_message = await message.answer("Ma'lumot yuklanmoqda...✍️💬")
    tiktok_data = tiktok_save(link)  # TikTok ma'lumotlarini olish
    await loading_message.delete()
    video = tiktok_data.get("video")
    music = tiktok_data.get("music")
    rasmlar = tiktok_data.get("images")
    
    # Rasmlarni yuborish
    if rasmlar: 
        rasm = []
        for i, r in enumerate(rasmlar):
            if not r.startswith("http"):
                print(f"Rasm URL noto'g'ri: {r}")
                continue
            rasm.append(InputMediaPhoto(media=r))
            if (i + 1) % 10 == 0:
                await message.answer_media_group(rasm)
                rasm = []
        if rasm:
            await message.answer_media_group(rasm)
    
    # Videoni yuborish
    if video:
        if not video.startswith("http"):
            print(f"Video URL noto'g'ri: {video}")
        else:
            await message.answer_video(video=video)
    
    # Musiqani yuborish
    if music: 
        if not music.startswith("http"):
            print(f"Audio URL noto'g'ri: {music}")
        else:
            await message.answer_audio(audio=music)


@dp.message(F.text.contains("pin"))
async def pinterest_download(message:Message):
    link = message.text
    try:
        loading_message = await message.answer("Ma'lumot yuklanmoqda...✍️💬")
        download_link = pinterest_save(link)
        await loading_message.delete()
        await message.reply(f"Mana yuklab olish havolasi: {download_link}")
    except Exception as e:
        await message.reply("Uzr, havolani yuklab olishda xatolik yuz berdi.")

#bot ishga tushganini xabarini yuborish
@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)

#bot ishdan to'xtadi xabarini yuborish
@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from middlewares.throttling import ThrottlingMiddleware

    # Spamdan himoya qilish uchun klassik ichki o'rta dastur. So'rovlar orasidagi asosiy vaqtlar 0,5 soniya
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))



async def main() -> None:
    await set_default_commands(bot)
    db.create_table_users()
    setup_middlewares(dispatcher=dp, bot=bot)
    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())