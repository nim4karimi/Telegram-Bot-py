from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'In Peygham az Robot miad va eme to hast --> {}'.format(update.message.from_user.first_name))


updater = Updater('543769920:AAFmM9qj3OzASYU70Hie2eqzwhpOfwQSM88')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(CommandHandler('first', first))


updater.start_polling()
updater.idle()