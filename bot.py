

import telebot, json;

bot = telebot.TeleBot('5846355673:AAE5c2BCXxBCc7aBExiTnhes8gaJKOapuvA');


sm = []
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Здесь можно написать команду. Например напиши: привет!")
    if str(message.text).lower() == "/save":
        bot.send_message(message.from_user.id, "What do you wanna save?")
        sm.append( str(message.text).lower() )
    elif str(message.text).lower() == "/load":
       bot.send_message(message.from_user.id, ( sm )) 

        

bot.polling(none_stop=True, interval=0)
