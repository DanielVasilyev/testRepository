import telebot, json;

bot = telebot.TeleBot('5846355673:AAE5c2BCXxBCc7aBExiTnhes8gaJKOapuvA');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Здесь можно написать команду. Например напиши: привет!")
    if str(message.text).lower() == "/save":
        bot.send_message(message.from_user.id, "What do you wanna save?")
        while str(message.text).lower() != "/end":
            str1 = str(message.text).lower()
            with open("files.json", "w") as outfile:
                json.dump(files, outfile)
    elif str(message.text).lower() == "/load":
        with open("files.json") as json_file:
            files = json.load(json_file)
            for i in files["str0"]:
                bot.send_message(message.from_files.json, i["str1"])
                bot.send_message(message.from_files.json, i["str2"])
                bot.send_message(message.from_files.json, i["str3"])
                bot.send_message(message.from_files.json, i["str4"])
                bot.send_message(message.from_files.json, i["str5"])
                bot.send_message(message.from_files.json, i["str6"])
                bot.send_message(message.from_files.json, i["str7"])
                bot.send_message(message.from_files.json, i["str8"])
                bot.send_message(message.from_files.json, i["str9"])
                bot.send_message(message.from_files.json, i["str10"])

        

bot.polling(none_stop=True, interval=0)