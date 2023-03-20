import logging

from aiogram import Bot, Dispatcher, executor, types

from sh import sh, shController

API_TOKEN = '5756193644:AAG0zb9XHi7g2x6qrnvA0TrccpnfU6G2RUE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


shs = [
    sh('1. Строение атома', 'Описание', ['./img/1.jpg', './img/8.jpg']),
    sh('2. Закономерности измения свойств по периодам и группам', 'описание', ['./img/2.jpg','./img/9.jpg']),
    sh('3. Валентности', 'описание', ['./img/3.jpg','./img/10.jpg']),
    sh('4. Типы химических связей', 'описание', ['./img/4.jpg','./img/11.jpg']),
    sh('5. Классификация химических реакций', 'описание', ['./img/5.jpg','./img/12.jpg']),
    sh('6. Основные формулы', 'описание', ['./img/6.jpg','./img/13.jpg']),
    sh('7. Мотивация', 'описание', ['./img/7.jpg'])

]

controller = shController(shs)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Главное меню', reply_markup=controller.getStartMenu())

@dp.message_handler()
async def send_command(message: types.Message):
    t = controller.getSh(message.text)
    if t.image == None:
        await message.reply(t.message, reply_markup=t.kb)
        return
    photo = open(t.image, 'rb')
    await message.reply_photo(photo=photo, caption=t.message, reply_markup=t.kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)