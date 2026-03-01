import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)
from aiogram.filters import Command

BOT_TOKEN = "8629206474:AAHYCgnIZ-FApZBzmIsfnzQdXnePqgoDVAs"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Открыть мини‑приложение",
                    web_app=WebAppInfo(url="https://lucky-kataifi-a43bb5.netlify.app"),
                )
            ]
        ]
    )

    await message.answer(
        "✅ Бот работает!\n\nНажми кнопку ниже:", reply_markup=keyboard
    )


# ✅ ОБРАБОТЧИК ДАННЫХ ИЗ MINI APP
@dp.message()
async def handle_all_messages(message: Message):
    print("RAW MESSAGE:", message)

    if message.web_app_data:
        data = message.web_app_data.data
        print("Получены данные:", data)
        await message.answer(f"✅ Получил данные: {data}")
    else:
        print("Обычное сообщение")


async def main():
    print("Бот запущен ✅")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
