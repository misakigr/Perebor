# import csv, sqlite3
#
# con = sqlite3.connect('partners.db')
# cur = con.cursor()
# cur.execute("""CREATE TABLE friends (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             area TEXT
# )""")
#
# with open('input.csv','r', encoding="utf8") as f:
#     dr = csv.DictReader(f, delimiter=";")
#     to_db = [(i['name'], i['area']) for i in dr]
#
# cur.executemany("INSERT INTO friends (name, area) VALUES (?, ?);", to_db)
# con.commit()
# con.close()


import sqlite3
import SendDock


db = sqlite3.connect('partners.db')
Connection = sqlite3.connect(':memory:')
db.backup(Connection)
sql = Connection.cursor()
db.close()

def dbaza(name, wallet):
    sql.execute("SELECT name FROM friends WHERE name = ?", [name])
    if sql.fetchone() is None:
        #print('Нет?')
        pass
    else:
        print('Да!',name)
        SendDock.send(wallet)