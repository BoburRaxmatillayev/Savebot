from filters.check_sub_channel import IsCheckSubChannels
from loader import bot,db,dp,CHANNELS,ADMINS
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message,InlineKeyboardButton
from aiogram.filters import Command
from filters.admin import IsBotAdminFilter
from states.reklama import Adverts
from aiogram.fsm.context import FSMContext #new
from keyboard_buttons import admin_keyboard
import time 
from aiogram import F


@dp.message(IsCheckSubChannels())
async def kanalga_obuna(message:Message):
    text = ""
    inline_channel = InlineKeyboardBuilder()
    for index,channel in enumerate(CHANNELS):
        ChatInviteLink = await bot.create_chat_invite_link(channel)
        inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal",url=ChatInviteLink.invite_link))
    inline_channel.adjust(1,repeat=True)
    button = inline_channel.as_markup()
    await message.answer(f"{text} kanallarga azo bo'ling",reply_markup=button)



#help commands
@dp.message(Command("/help"))
async def help_commands(message:Message):
    await message.answer("🤖 All Saver может скачать для вас видео ролики и аудио из\n популярных социальных сетей.\nКак пользоваться:\n 1. Зайдите в одну из социальных сетей.\n  2. Выберите интересное для вас видео.\n  3. Нажми кнопку «Скопировать».\n  4. Отправьте нашему боту и получите ваш файл!\nБот может скачивать с:\n1. TikTok (https://www.tiktok.com/)\n  2. YouTube (https://www.youtube.com/)\n 3. Pinterest (https://www.pinterest.com/)\n  4. Instagram (https://www.instagram.com/)")



#lang commands
@dp.message(Command("/lang"))
async def about_commands(message:Message):
    await message.answer("🇷🇺 Выберите язык]n🏴󠁧󠁢󠁥󠁮󠁧󠁿 Choose language\n🇺🇿 Tilni tanlang")


@dp.message(Command("/admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)


@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()

