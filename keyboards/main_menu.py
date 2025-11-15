from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    kb = [
        [KeyboardButton(text="📤 Тестовый пост")],
        [KeyboardButton(text="📅 Планировщик (демо)")],
        [KeyboardButton(text="📂 Импорт из Excel")],
        [KeyboardButton(text="⚙ Настройки")],
        [KeyboardButton(text="ℹ О боте")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
