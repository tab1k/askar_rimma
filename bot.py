import telebot
from telebot import types

import config
from additional import *

bot = telebot.TeleBot(config.TOKEN)

itsme = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
itsme.row('Это я, Римма 😌')


@bot.message_handler(commands=['start'])
def start_message(message):
    sti = open('anime.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,
                     f'Привет👋🏻  *{message.from_user.first_name}* !\n - этот Бот создан для моей Риммочки 😌',
                     parse_mode="Markdown", reply_markup=itsme)
    bot.register_next_step_handler(message, continue_start_message)


def continue_start_message(message):
    if message.text == 'Это я, Римма 😌':
        bot.send_message(message.chat.id, 'Привет, ботам 😘', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Как дела?')
        bot.register_next_step_handler(message, how_are_u)


def how_are_u(message):
    if message.text in good:
        bot.send_message(message.chat.id, 'Я очень рад, что у тебя все хорошо 😘🙃')
        bot.send_message(message.chat.id, 'Как прошел твой день? 😘')
        bot.register_next_step_handler(message, continue_message)
    if message.text in bad:
        bot.send_message(message.chat.id, 'Все будет хорошо, ботам 💋')
        bot.send_message(message.chat.id, 'Не переживай 😘')
        bot.send_message(message.chat.id, 'Ну ка, давай расскажи что случилось?)😘')
        bot.register_next_step_handler(message, continue_message5)



def continue_message(message):
    if message.text in good:
        bot.send_message(message.chat.id, 'Ну ка, давай рассказывай что такого было?) 😘🙃')
        bot.send_message(message.chat.id, good_nastr)
        bot.register_next_step_handler(message, continue_message2)


def continue_message2(message):
    bot.send_message(message.chat.id, 'Оке, начинай рассказывать) Я по уши во внимании 😊')
    bot.register_next_step_handler(message, continue_message3)


@bot.message_handler(content_types=["text"])
def continue_message3(message):
    if message.text == 'все' or 'Все':
        bot.send_message(message.chat.id, 'Очень интересно 😚')
        bot.send_message(message.chat.id, 'Но знай, все что не делается , делается к лучшему 😌')
        bot.register_next_step_handler(message, continue_message4)

    if message.text in message1:
        bot.send_message(message.chat.id, 'Какая ты у меня умница! 😍')
        bot.register_next_step_handler(message, continue_message4)


def continue_message4(message):
    bot.send_message(message.chat.id, 'Какие еще новости?')
    if message.text in news[0]:
        bot.send_message(message.chat.id, 'Оке. Тогда давай вспомним наши с тобой моменты)')
        bot.send_photo(message.chat.id, photo)
    if message.text in news[1]:
        bot.send_message(message, 'Слушаю)')


@bot.message_handler(content_types=["text"])
def continue_message5(message):
    sti2 = open('sti2.tgs', 'rb')
    bot.send_message(message.chat.id, 'Понимаю, все может быть в этом мире 😘')
    bot.send_message(message.chat.id, 'Не переживай)')
    bot.send_sticker(message.chat.id, sti2)
    bot.register_next_step_handler(message, continue_message6)


def continue_message6(message):
    bot.send_message(message.chat.id, 'Может это поднимет тебе настроение)')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, 'Если хочешь еще несколько фото увидеть , напиши - хочу ещё')
    bot.register_next_step_handler(message, photos)


@bot.message_handler(content_types=["text"])
def photos(message):
    if message.text == 'хочу ещё' or 'хочу еще':
        bot.send_photo(message.chat.id, photo2)
        bot.send_photo(message.chat.id, photo3)


@bot.message_handler(commands=['help'])
def send_settings(message):
    bot.send_message(message.chat.id, help)


bot.polling(none_stop=True, interval=0)
