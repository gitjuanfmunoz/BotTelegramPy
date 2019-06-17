import telegram 
from telegram.ext import *

mybot = telegram.Bot(token="XXXXX") # cambias las XXXXX por tu Token
mybot_updater = Updater(mybot.token)


def start(bot, update, pass_chat_data=True):
	update.message.chat_id
	bot.send.Message(chat_id=update.message.chat_id, text="gracias por escribir!")

start_handler = CommandHandler('start', start)

dispatcher =mybot_updater.dispatcher

dispatcher.add_handler(start_handler)

mybot_updater.start_polling()
mybot_updater.idle()

while True:
	pass

