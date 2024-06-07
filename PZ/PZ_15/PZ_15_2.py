# Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для некоторой организации. БД
# должна содержать таблицу Работник со следующей структурой записи: фамилия, имя,
# отчество, возраст, пол, профессия, стаж работы.

import sqlite3

conn = sqlite3.connect('workers.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Работник (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        фамилия TEXT,
        имя TEXT,
        отчество TEXT,
        возраст INTEGER,
        пол INTEGER,
        профессия TEXT,
        стаж_работы TEXT
    )
''')

from workers_data import w_data

for worker in w_data:
    cursor.execute('''
        INSERT INTO Работник (фамилия, имя, отчество, возраст, пол, профессия, стаж_работы)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', worker)

conn.commit()
conn.close()

from workers_data import w_data

print("{:<10} {:<10} {:<10} {:<5} {:<5} {:<15} {:<10}"
      .format('Фамилия', 'Имя', 'Отчество', 'Возраст', 'Пол', 'Профессия', 'Стаж'))

for worker in w_data:
    print("{:<10} {:<10} {:<10} {:<5} {:<5} {:<15} {:<10}"
          .format(worker[0], worker[1], worker[2], worker[3], worker[4], worker[5], worker[6]))