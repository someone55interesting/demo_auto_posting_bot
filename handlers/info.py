from aiogram import Router, F
from aiogram.types import Message

router = Router()

def register_info():
    return router

@router.message(F.text == "ℹ О боте")
async def info(message: Message):
    await message.answer(
        "<b>🤖 DEMO AutoPoster Bot</b>\n\n"
        "Автопостинг, расписание, Excel импорт.\n"
        "Часть функций ограничена специально.\n\n"
        "Хотите такой же полноценный бот?\n"
        "Напишите: <b>Хочу бота</b> 🔥"
    )
