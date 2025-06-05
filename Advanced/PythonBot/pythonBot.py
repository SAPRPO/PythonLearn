from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')
    print('message sended')
token_user="7749266941:AAGcJC35lYcPJp__WG8Ht_Tusl8Eio02XKI"
app = ApplicationBuilder().token(token_user).build()

app.add_handler(CommandHandler("hello", hello))



app.run_polling()


