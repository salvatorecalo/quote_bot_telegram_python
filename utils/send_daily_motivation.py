from telegram.ext import ContextTypes
from .get_all_user import get_all_users
from random import randint

QUOTES = [
    "So che ce la puoi fare campione ",
    "Non mollare, sei più forte di quanto pensi!",
    "Ogni giorno è una nuova opportunità per crescere e migliorare.",
    "La tua forza interiore è più grande di qualsiasi ostacolo.",
    "Credi in te stesso e tutto sarà possibile.",
]
async def send_daily_motivation(context: ContextTypes.DEFAULT_TYPE):
    """Sends a daily motivational quote to the user."""
    random_index = randint(0, len(QUOTES) - 1)
    all_users = get_all_users()
    for user_id in all_users:
        await context.bot.send_message(chat_id=user_id, text=QUOTES[random_index])    