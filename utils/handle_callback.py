from telegram import Update
from telegram.ext import ContextTypes
from utils.setup_logger import setup_logger
from utils.start_command import start_command

logger = setup_logger(__name__)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update or not update.callback_query:
        logger.error("Invalid update object received in handle_callback.")
        return
    query = update.callback_query
    await query.answer()
    data = query.data
    if not data:
        return 
    logger.info(f"Received callback query with data: {data}")
    if data == "start":
        await start_command(update, context)
    