from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import qrcode
from io import BytesIO

TOKEN = '7972124480:AAGgPIfwfllX744dZk39QVaRF-wou8eBQyA'  # bot token

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me any text or URL and I will generate a QR code for it!")

# Function to handle messages (QR code generation)
async def generate_qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Generate QR code
    qr_img = qrcode.make(text)
    bio = BytesIO()
    bio.name = "qr.png"
    qr_img.save(bio, "PNG")
    bio.seek(0)

    # Send image back
    await update.message.reply_photo(photo=bio, caption="Here is your QR Code 📷")

# Main function to start the bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_qr))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
