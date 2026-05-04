from telegram import Update
from telegram.ext import ContextTypes
from utils.save_user_to_db import save_user_to_db
from utils.setup_logger import setup_logger

logger = setup_logger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Start command received")
    if not update or not update.effective_chat or not update.effective_user:
        logger.error("Invalid update object received in start_command.")
        return
    save_user_to_db(update.effective_user.id)
    user_name = update.effective_user.first_name
    await update.effective_message.reply_text(f"Hello {user_name}, welcome to the bot, here you can feel better with yourself!")
    