import telebot  # import the pyTelegramBotAPI module
import conf     # import your API token

bot = telebot.TeleBot(conf.TOKEN)  # create bot

# This handler runs function send_welcome, when user texts /start or /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hi! This is a bot that counts the length of your message in symbols!")

@bot.message_handler(func=lambda m: True)  # This handles any sort of messages
def send_len(message):
	bot.send_message(message.chat.id, 'Your message has {} symbols.'.format(len(message.text)))

# @bot.message_handler(???) # describe what sort of messages trigger the function 
# def my_function(message):
#     reply = '' 
#     ??? # here is the code to generate the reply
# 	bot.send_message(message.chat.id, reply)  # send reply back to the chat

if __name__ == '__main__':
    bot.polling(none_stop=True)