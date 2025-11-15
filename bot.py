import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from keyboards.main_menu import main_menu
from handlers.post_demo import register_post_demo
from handlers.scheduler_demo import register_scheduler_demo
from handlers.excel_demo import register_excel_demo
from handlers.settings_demo import register_settings_demo
from handlers.info import register_info
from utils.anti_pirate import check_owner

TOKEN = "8513624083:AAFBHdvgkT2GPc0XJgmyoIPsbQd8pRlT6dE"
OWNER_ID = 5134857973 # ← твой Telegram ID. Без него никто не сможет украсть бота.

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    if not await check_owner(message, OWNER_ID):
        return

    await message.answer(
        "<b>👋 Привет! Это DEMO AutoPoster Bot</b>\n\n"
        "🔸 Автопостинг\n"
        "🔸 Планировщик\n"
        "🔸 Excel импорт\n"
        "🔸 Настройки\n\n"
        "Часть функций ограничена, так как это демо-версия.",
        reply_markup=main_menu()
    )


async def main():
    dp.include_routers(
        register_post_demo(),
        register_scheduler_demo(),
        register_excel_demo(),
        register_settings_demo(),
        register_info(),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
