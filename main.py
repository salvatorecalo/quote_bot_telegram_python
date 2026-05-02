from utils import setup_logger, handle_callback, start_command, send_daily_motivation, create_user_table
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler
from dotenv import load_dotenv
import os
import datetime
import pytz

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
        hours = datetime.time(hour=22, minute=31, second=0, tzinfo=pytz.timezone('Europe/Rome'))
        job_queue.run_daily(send_daily_motivation, time=hours)
        
        app.run_polling()
        if app.updater.running:
            logger.info("Bot is running.")
    except Exception as e:
        logger.error(f"Error occurred while building the application: {e}")

if __name__ == "__main__":
    main()