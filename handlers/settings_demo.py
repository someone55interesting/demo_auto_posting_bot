from aiogram import Router, F
from aiogram.types import Message

router = Router()

def register_settings_demo():
    return router

@router.message(F.text == "⚙ Настройки")
async def settings_demo(message: Message):
    await message.answer(
        "⚙ <b>Настройки (DEMO)</b>\n\n"
        "Настройка канала, задержек, автоудаления и др.\n"
        "В полной версии доступно."
    )
