from threading import Thread

from utils import setup_logger, handle_callback, start_command, send_daily_motivation, create_user_table
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler
from dotenv import load_dotenv
import os
import datetime
import pytz
# I import flask just because leapcell is looking for a web server to run the bot :(
from flask import Flask

web_server = Flask(__name__)

@web_server.route('/')
def home():
    return "Hello, this is the home page of the bot!"

# this route is used only by leapcell to check if the bot is alive
@web_server.route("/kaithhealthcheck")
def health_check():
    return "OK", 200

def run_bot():
    web_server.run(host="0.0.0.0", port=8080)

# Here we put our basic bot stuff
load_dotenv()
logger = setup_logger(__name__)

def main():
    logger.info("Bot has started.")
    try:
        create_user_table()
        app = ApplicationBuilder().token(os.getenv("TOKEN")).build()
        
        app.add_handler(CallbackQueryHandler(handle_callback))
        app.add_handler(CommandHandler("start", start_command))
        
        job_queue = app.job_queue
        hours = datetime.time(hour=11, minute=48, second=0, tzinfo=pytz.timezone('Europe/Rome'))
        job_queue.run_daily(send_daily_motivation, time=hours)
        
        app.run_polling()
        if app.updater.running:
            logger.info("Bot is running.")
    except Exception as e:
        logger.error(f"Error occurred while building the application: {e}")

if __name__ == "__main__":
    # I moved it here because I want to run it only one time, also if it was in the previous position in was run only one time because you cannot import main n other files
    Thread(target=run_bot).start()
    main()