# Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для некоторой организации. БД
# должна содержать таблицу Работник со следующей структурой записи: фамилия, имя,
# отчество, возраст, пол, профессия, стаж работы

import sqlite3 as sq

# Подключение к базе данных
con = sq.connect('Mamedove.db')
with con:
    cur = con.cursor()
    
    # Создание таблицы workers
    cur.execute("""CREATE TABLE IF NOT EXISTS workers (
    id_work INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR,
    first_name VARCHAR,
    middle_name VARCHAR,
    age INTEGER,
    gender VARCHAR,
    profession VARCHAR,
    experience INTEGER
    )""")
  
    # Функция добавления нового работника
    def add_worker(last_name, first_name, middle_name, age, gender, profession, experience):
        cur.execute("INSERT INTO workers(last_name, first_name, middle_name, age, gender, profession, experience) VALUES(?,?,?,?,?,?,?)",
                    (last_name, first_name, middle_name, age, gender, profession, experience))
        con.commit()

    # Функция вывода всех работников
    def get_worker():
        cur.execute("SELECT * FROM workers")
        result = cur.fetchall()
        for row in result:
            print(row)

    # Пример добавления работников
    add_worker('Иванов', 'Иван', 'Иванович', 25, 'М', 'Программист', 3)
    add_worker('Матвеев', 'Алексей', 'Олегович', 29, 'М', 'Тим-лид', 9)
    # Добавление других работников здесь
    
    # Выборка работников по критериям
    get_worker()  # Все работники

    cur.execute('SELECT * FROM workers WHERE age > 26')
    print(cur.fetchall())  # Работники старше 26 лет

    cur.execute('SELECT * FROM workers WHERE profession = "Программист"')
    print(cur.fetchall())  # Программисты

    cur.execute('SELECT * FROM workers WHERE experience > 7 AND experience < 20')
    print(cur.fetchall())  # С опытом от 8 до 19 лет

    # Удаление работников по критериям
    cur.execute('DELETE FROM workers WHERE age > 27 AND age < 45')
    con.commit()

    cur.execute('DELETE FROM workers WHERE experience < 5')
    con.commit()

    cur.execute('DELETE FROM workers WHERE first_name = "Александр"')
    con.commit()

    # Обновление данных о работниках
    cur.execute('UPDATE workers SET last_name="Петрова" WHERE last_name="Иванова"')
    con.commit()

    cur.execute('UPDATE workers SET age=31 WHERE last_name="Григорьев"')
    con.commit()

    cur.execute('UPDATE workers SET profession="Главный-инженер" WHERE last_name="Петров"')
    con.commit()