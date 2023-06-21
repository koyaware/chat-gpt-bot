import openai
from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.config import load_config


async def user_start(message: Message):
    await message.reply("Hello, user!")


async def chat_gpt(message: Message):
    config = load_config(".env")
    openai.api_key = config.OAIToken
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000
    )
    await message.answer(response['choices'][0]['text'])


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(chat_gpt)
