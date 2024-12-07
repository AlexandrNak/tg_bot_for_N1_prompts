from aiogram import types, Router, F
from aiogram.filters.command import Command
from hi_text import hi_post
from tg_bot_main import bot

from keyboards import (inline_keyboard_start,
                       inline_keyboard_promt_library,
                       category_kb,
                       inline_kd_project_news,
                       inline_check_kb,
                       inline_ii_model_kb,
                       inline_develop_creativity_kb
                       )

router = Router()

CHANNEL_ID = "@test_n1_prompts"
ADMIN_ID = "1084391475"
ADMIN_ID_1 = "@Alexandr_Nakaryakov"

# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(hi_post, reply_markup=inline_keyboard_start)

# Хэндлер на команду /support
@router.message(Command("support"))
async def support(message: types.Message):
    await message.answer("Напишите и отправьте свой вопрос")

@router.message()
async def text_support(message: types.Message):
    # print(message.from_user.id)
    await bot.forward_message(chat_id=CHANNEL_ID, 
                            from_chat_id=message.from_user.id, 
                            message_id=message.message_id)
    await message.reply("Ваше сообщение отправлено! Администратор скоро свяжется с вами")

@router.callback_query(F.data == 'start')
async def cmd_start_back(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(hi_post, reply_markup=inline_keyboard_start)

# Ответ на кнопку Библиотека промтов
@router.callback_query(F.data == 'promt_library')
async def promt_library(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(
        "Создай свой промт или выбери из библиотеки 👇", 
        reply_markup=inline_keyboard_promt_library)

# Ответ на кнопку Промты по категориям
@router.callback_query(F.data == 'category_promt')
async def category_promt(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(
        "Выбери категорию 👇", 
        reply_markup=category_kb)

# Ответ на кнопку Новости проекта с проверкой подписки
@router.callback_query(F.data == 'project_news')
async def project_news(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=callback.from_user.id)
    if sub.status != "left":
        await callback.message.answer(
                "Следите за новостями проекта на нашем канале 👇", 
                reply_markup=inline_kd_project_news)
    else:
        await callback.message.answer(
                "Для доступа подпишитесь на канал 👇",
                reply_markup=inline_check_kb)
    
# Ответ на кнопку ИИ-модели с проверкой подписки
@router.callback_query(F.data == 'ii_model')
async def ii_model(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=callback.from_user.id)
    if sub.status != "left":
        await callback.message.answer(
                "Выбери ИИ-модель 👇 кнопки не работают, кроме НАЗАД", 
                reply_markup=inline_ii_model_kb)
    else:
        await callback.message.answer(
                "Для доступа подпишитесь на канал 👇", 
                reply_markup=inline_check_kb)

@router.callback_query(F.data == 'develop_creativity')
async def develop_creativity(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(
            "Я не разбираюсь в искусстве и творчестве, но хочу найти хобби для развития креативности с низким порогом вхождения. Подготовь мне список вариантов и укажи, какие материалы понадобятся для каждого вида творчества",
            reply_markup=inline_develop_creativity_kb)

@router.callback_query(F.data == 'copy_promt')
async def copy_promt(callback: types.CallbackQuery):
    await callback.answer()
