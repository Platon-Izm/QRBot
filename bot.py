import telebot
import qrcode
#getting a token from a text file
file = open('token.txt', 'r', encoding='utf-8')
token = file.read()
file.close()
bot = telebot.TeleBot(token)
#start
@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['start'])

#command receive function
def qr (message):
    #get the radius from the message
    text=str(message.text)
    qr=open('qr.png', 'w')
    image=qrcode.make(text)
    image.save('qr.png')
    qr.close()
    bot.send_photo(message.from_user.id, photo=open('qr.png', 'rb'))

#run
bot.polling(none_stop=True)