import telebot
from telebot import types


token = '6948724685:AAE2lMMd3w6wtiSoSR8KvsjmnuZX9qXcRYA'
bot = telebot.TeleBot(token)


# напишем функцию для создания наших кнопок
def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу пить', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть', callback_data='2')
    walk_btn = types.InlineKeyboardButton(text='Хочу гулять', callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text='Хочу спать', callback_data='4')
    joke_btn = types.InlineKeyboardButton(text='Хочу шутку', callback_data='5')
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(walk_btn)
    keyboard.add(sleep_btn)
    keyboard.add(joke_btn)
    return keyboard


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        'Добрый день!',
        reply_markup=keyboard
    )



if __name__ == '__main__':
    bot.polling(none_stop=True)