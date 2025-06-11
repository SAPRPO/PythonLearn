from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN='7749266941:AAGcJC35lYcPJp__WG8Ht_Tusl8Eio02XKI'

#objects for bot and dispatcher

bot = Bot(token=API_TOKEN)
dp =Dispatcher(bot)

#Handler for incomig messages
dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
