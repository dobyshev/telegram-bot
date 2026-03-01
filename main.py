import os
from aiohttp import web
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_PATH = "/webhook"
BASE_WEBHOOK_URL = "https://telegram-bot-2f7l.onrender.com"
WEBHOOK_URL = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Открыть мини‑приложение",
                    web_app=WebAppInfo(
                        url="ТВОЯ_NETLIFY_ССЫЛКА"
                    )
                )
            ]
        ]
    )

    await message.answer("Бот работает через webhook ✅", reply_markup=keyboard)


@dp.message(F.web_app_data)
async def handle_webapp(message: Message):
    data = message.web_app_data.data
    await message.answer(f"✅ Получил данные: {data}")


async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(app):
    await bot.delete_webhook()


def main():
    app = web.Application()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.run_webhook(
        webhook_path=WEBHOOK_PATH,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
    )


if __name__ == "__main__":
    main()
