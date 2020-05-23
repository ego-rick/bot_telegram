import telebot

bot = telebot.TeleBot("1242336019:AAHOF5MZ3Xib-WNslNhIkE9iIqFA2vaUsRg")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
bot.polling()
