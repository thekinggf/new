
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN")
updater = Updater( Token ,use_context = True )

def start(updater,context):
