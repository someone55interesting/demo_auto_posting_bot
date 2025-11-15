from aiogram.types import Message

async def check_owner(message: Message, owner_id: int):
    if message.from_user.id != owner_id:
        await message.answer(
            "⛔ Этот бот — DEMO версия.\n"
            "Доступ разрешён только владельцу."
        )
        return False
    return True
