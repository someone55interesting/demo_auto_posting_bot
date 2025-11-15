from aiogram import Router, F
from aiogram.types import Message

router = Router()

def register_post_demo():
    return router

@router.message(F.text == "📤 Тестовый пост")
async def ask_post(message: Message):
    await message.answer("Отправьте текст поста:")

@router.message(F.text & ~F.text.in_(
    ["📤 Тестовый пост", "📅 Планировщик (демо)",
     "📂 Импорт из Excel", "⚙ Настройки", "ℹ О боте"]
))
async def echo_post(message: Message):

    await message.answer(
        "<b>✨ Ваш пост (демо):</b>\n\n"
        f"{message.text}\n\n"
        "В полной версии — бот отправит это в канал!"
    )
