from telegram import Update
from telegram.ext import Application, CommandHandler
import logging
import config  # Файл с токеном бота

# Логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Список участников с уникальными токенами
participants = {
    "unique_token_1": "Maksym",
    "unique_token_2": "Nikita",
    "unique_token_3": "Solomia",
    "unique_token_4": "Anton",
    "unique_token_5": "Sasha"
}

# Хранилище для отслеживания состояния участников
checked_in = set()

# Функция обработки команды /start
async def start(update: Update, context):
    # Проверяем, есть ли параметры
    if context.args:
        # Получаем первый параметр
        parameter = context.args[0]
        # Логируем параметр для проверки
        logging.info(f"Received parameter: {parameter}")

        # Проверяем, является ли параметр токеном
        if parameter in participants:
            participant_name = participants[parameter]
            if parameter not in checked_in:
                checked_in.add(parameter)
                await update.message.reply_text(
                    f"✅ 🎉 *{participant_name}* пришел на мероприятие! 🥳",
                    parse_mode='Markdown'
                )
            else:
                await update.message.reply_text(
                    f"🚫 *{participant_name}* уже зарегистрирован. 🚫",
                    parse_mode='Markdown'
                )
        else:
            await update.message.reply_text(
                "❌ Этот билет не найден. ❌"
            )
    else:
        await update.message.reply_text(
            "🤖 Бот запущен и ожидает переходов по ссылкам. 🤖"
        )

# Основная функция для запуска бота
def main():
    # Инициализация бота с токеном
    application = Application.builder().token(config.tg_bot_token).build()

    # Обработчик команды /start для запуска бота и обработки ссылок
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
