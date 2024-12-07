from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

support_kb = [
    [KeyboardButton(text='Поддержка')]
]
support_kb_start = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=support_kb)

inline_kb_start = [
    [InlineKeyboardButton(text="Библиотека промтов", 
                          callback_data="promt_library")],
    [InlineKeyboardButton(text="ИИ-модели", 
                          callback_data="ii_model")],
    [InlineKeyboardButton(text="Новости проекта", 
                          callback_data="project_news")],
]
inline_keyboard_start = InlineKeyboardMarkup(inline_keyboard=inline_kb_start)


inline_kb_promt_library = [
    [InlineKeyboardButton(text="Промты по категориям", 
                          callback_data="category_promt")],
    [InlineKeyboardButton(text="Персональная подборка промтов", 
                          callback_data="lib")],
    [InlineKeyboardButton(text="<<  Назад", 
                          callback_data="start")],
]
inline_keyboard_promt_library = InlineKeyboardMarkup(
    inline_keyboard=inline_kb_promt_library)


category = [
    [InlineKeyboardButton(text="Развить креативность", 
                          callback_data="develop_creativity")],
    [InlineKeyboardButton(text="Кнопка не работает", 
                          callback_data="cdwcd")],
    [InlineKeyboardButton(text="Кнопка не работает", 
                          callback_data="vdfvd")],
    [InlineKeyboardButton(text="<<  Назад", 
                          callback_data="promt_library")],
]
category_kb = InlineKeyboardMarkup(inline_keyboard=category)

project_news_kb = [
    [InlineKeyboardButton(text="Наш канал", 
                          url="https://t.me/test_n1_prompts")],
    [InlineKeyboardButton(text="<<  Назад", 
                          callback_data="start")],
]
inline_kd_project_news = InlineKeyboardMarkup(inline_keyboard=project_news_kb)

check_kb = [
    [InlineKeyboardButton(text="Подписаться", url="https://t.me/test_n1_prompts")],
    [InlineKeyboardButton(text="<< Назад", callback_data="start")]
]
inline_check_kb = InlineKeyboardMarkup(inline_keyboard=check_kb)

ii_model_kb = [
    [InlineKeyboardButton(text="GPT 4o", 
                          callback_data="lib")],
    [InlineKeyboardButton(text="Llama", 
                          callback_data="cdwcd")],
    [InlineKeyboardButton(text="Midjorney", 
                          callback_data="vdfvd")],
    [InlineKeyboardButton(text="Flux", 
                          callback_data="vdfvd")],
    [InlineKeyboardButton(text="<<  Назад", 
                          callback_data="start")],
]
inline_ii_model_kb = InlineKeyboardMarkup(inline_keyboard=ii_model_kb)

develop_creativity_kb = [
    [InlineKeyboardButton(text="Копировать промт", 
                          callback_data="copy_promt")],
    [InlineKeyboardButton(text="<<  Назад", 
                          callback_data="category_promt")],
]
inline_develop_creativity_kb = InlineKeyboardMarkup(inline_keyboard=develop_creativity_kb)