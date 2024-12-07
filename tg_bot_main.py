from aiogram import Bot, Dispatcher
import asyncio
import logging
from aiogram.types import BotCommand, BotCommandScopeDefault
from config_reader import config

import handlers

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()

async def set_commands():
    commands = [
                BotCommand(command='start', description='Старт'),
                BotCommand(command='support', description='Поддержка')
                ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_routers(handlers.router)
    await dp.start_polling(bot)
    await set_commands()
    
if __name__ == "__main__":
    asyncio.run(main())

