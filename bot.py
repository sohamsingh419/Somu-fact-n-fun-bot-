import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("")
OWNER_ID = int(os.getenv("OWNER_ID", "5962449368"))  # Replace with your ID or use env var

CHANNEL_LINK = "https://t.me/fact_and_fun"
GROUP_LINK = "https://t.me/fact_fun18"

# /start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Welcome {update.effective_user.first_name}!\n\n"
        f"Join our Channel: {Chttps://t.me/fact_and_fun}\n"
        f"Join our Group: {https://t.me/fact_fun18}"
    )

# /post handler for owner only
async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return await update.message.reply_text("You are not authorized to use this command.")
    
    if not context.args:
        return await update.message.reply_text("Usage: /post <message>")
    
    message = " ".join(context.args)

    # Get all chat IDs where bot is admin
    sent_to = 0
    async for dialog in context.bot.get_updates():
        try:
            await context.bot.send_message(chat_id=dialog.message.chat_id, text=message)
            sent_to += 1
        except:
            pass

    await update.message.reply_text(f"Posted in {sent_to} chats.")

# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post", post))
    app.run_polling()

if __name__ == "__main__":
    main()
