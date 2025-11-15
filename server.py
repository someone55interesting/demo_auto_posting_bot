import os
import asyncio
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.enums import ParseMode

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Импортируем наши маршруты
from handlers.post_demo import router as post_router
from handlers.scheduler_demo import router as scheduler_router
from handlers.excel_demo import router as excel_router
from handlers.settings_demo import router as settings_router
from handlers.info import router as info_router

dp.include_router(post_router)
dp.include_router(scheduler_router)
dp.include_router(excel_router)
dp.include_router(settings_router)
dp.include_router(info_router)

app = FastAPI()

@app.post("/")
async def webhook(request: Request):
    data = await request.json()
    update = Update(**data)
    await dp.feed_update(bot, update)
    return {"status": "ok"}

@app.on_event("startup")
async def on_startup():
    print("BOT STARTED")