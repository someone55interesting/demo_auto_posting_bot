from aiogram import Router, F
from aiogram.types import Message

router = Router()

def register_scheduler_demo():
    return router

@router.message(F.text == "📅 Планировщик (демо)")
async def scheduler_info(message: Message):
    await message.answer(
        "⏰ <b>ПЛАНИРОВЩИК (DEMO)</b>\n\n"
        "Вы можете задать расписание публикаций, но запуск в DEMO отключён.\n\n"
        "<i>Полная версия умеет публиковать посты по времени!</i>"
    )
