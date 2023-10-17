import telebot

from omaviat_calendar.config import bot


@bot.message_handler(commands=["start"])
async def _send_start_message(message) -> None:
    await bot.send_message(message.chat.id, "test")


@bot.message_handler(commands=["start_reg"])
async def _send_start_reg_message(message) -> None:
    options = []

    options.append(telebot.types.KeyboardButton("one"))
    options.append(telebot.types.KeyboardButton("two"))
    options.append(telebot.types.KeyboardButton("three"))

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    for option in options:
        markup.add(option)

    await bot.send_message(message.chat.id, "Choice number!", reply_markup=markup)


@bot.message_handler(content_types="text")
def _message_reply(message):
    if message.text == "one":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "")
