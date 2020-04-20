import telebot;
bot = telebot.TeleBot('1037152464:AAELNfqllvp9UEg9hkDkoG21lhAUMGaucT0');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")


bot.polling(none_stop=True, interval=0)