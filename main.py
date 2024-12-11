# main.py
from aiogram import executor
from config import bot, dp, Admins
import logging
from handlers import commands, echo, quiz, fsm_reg, fsm_shop
import buttons


async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот запущен!',
                               reply_markup=buttons.start_markup)

async def on_shutdown(_):
    await bot.send_message(chat_id=5576961334, text='Бот остановлен!')

commands.register_commands_handlers(dp)
quiz.register_quiz_handlers(dp)
fsm_reg.register_handlers_fsm_reg(dp)
fsm_shop.register_handlers_fsm_shop(dp)

echo.register_echo_handlers(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)


