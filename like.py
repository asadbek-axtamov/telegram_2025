import os
from telegram.ext import CommandHandler, Updater,MessageHandler
from telegram import Update

TOKEN = os.environ['TOKEN']
update_vote={"👍":0,"👎":0}
def like(update, context):
    
    if update.message.text=="👍" :
        update_vote['👍']+=1
    elif update.message.text=="👎"  :
        update_vote['👎']+=1
    update.message.reply_text(f"Like : {update_vote['👍']} Dislike : {update_vote['👎']}")

    

updater=Updater(TOKEN)
dispatcher=updater.dispatcher
dispatcher.add_handler(MessageHandler(filters=None, callback=like))
updater.start_polling()
updater.idle()