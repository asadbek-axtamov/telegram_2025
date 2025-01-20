import os
from telegram.ext import CommandHandler, Updater,MessageHandler
from telegram import Update

TOKEN = os.environ['TOKEN']

def echo(update: Update, context):

    update.message.reply_text(update.message.text)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(filters=None, callback=echo))

updater.start_polling()
updater.idle()