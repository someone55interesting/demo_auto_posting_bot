from aiogram import Router, F
from aiogram.types import Message

router = Router()

def register_excel_demo():
    return router

@router.message(F.text == "📂 Импорт из Excel")
async def excel_demo(message: Message):
    await message.answer(
        "📄 <b>Импорт Excel (DEMO)</b>\n\n"
        "В полной версии бот загружает Excel/CSV и создаёт очередь постинга.\n"
        "В демо эта функция отключена."
    )
