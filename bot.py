import telebot

bot = telebot.TeleBot("1191098101:AAF1gBSye1U2Tbx6-rUQPiWUPuCf15lZpnI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
bot.polling()
