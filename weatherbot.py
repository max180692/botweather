from curses import echo
from lib2to3.pgen2 import token
import logging
from aiogram import Bot, Dispatcher,executor,types
import settings
import parserweather as pw

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message:types.Message):
    await message.reply('Введите город')

@dp.message_handler()
async def echo1(message:types.Message):
    if message.text:
        result ='Погода в ' + message.text.title() + '\n' +   pw.get_weather_city(pw.get_city_url(message.text))
        await message.answer(result)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)

