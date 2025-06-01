from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я — Татьяна, архитектор и GSR-специалист.")
    await update.message.reply_text(
        "Если ты это читаешь — скорее всего, ты чувствуешь, что в твоём доме «что-то не так»."
    )
    await update.message.reply_text(
        "Вот PDF, с которого начинают мои клиенты. В нём 5 основных ошибок, из-за которых пространство может «давить», «мешать», «вызывать тревожность» или провоцировать отток энергии:"
    )
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open("5_errors_interior_state_detailed.pdf", "rb"))
    await update.message.reply_text(
        "Если после прочтения ты захочешь консультацию или GSR-разбор по планировке — пиши мне: @tm_ad_gsr"
    )
    await update.message.reply_text(
        "🔗 Канал о связи пространства и состояния: @tm_ad_gsr"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
