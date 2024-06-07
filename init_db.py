import sqlite3
def init_db():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS 'employees' (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'name' TEXT,
        'email' TEXT,
        'phone_number' TEXT,
        'position' TEXT,
        'department' TEXT,
        'chief_id' INTEGER
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS 'clients' (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'name' TEXT,
        'email' TEXT,
        'phone_number' TEXT,
        'passport' TEXT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS 'trainings' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'duration' INTEGER,
            'employee_id' INTEGER,
            'amount' INTEGER,
            'description' TEXT,
            'client_id' INTEGER
        )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS 'contracts' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'number' TEXT,
            'date' TEXT,
            'price' INTEGER,
            'discount' INTEGER,
            'deal_status' BLOB,
            'finish_price' INTEGER,
            'training_id' INTEGER,
            'client_id' INTEGER,
            'employee_id' INTEGER
        )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS 'reports' (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'number' TEXT,
        'date' TEXT,
        'report_type' TEXT,
        'description' TEXT,
        'employee_id' INTEGER
    )""")



    cur.execute("INSERT INTO 'employees' ('name', 'email', 'phone_number', 'position', 'department', 'chief_id')  VALUES (?, ?, ?, ?, ?, ?)",
                ('Петрова Полина Сергеевна', 'petrova@realtor.ru', '80001234567', 'тренер', 'отдел жилой недвижимости', 0))
    cur.execute("INSERT INTO 'clients' ('name', 'email', 'phone_number', 'passport')  VALUES (?, ?, ?, ?)",
                ('Соколова Галина Ивановна', 'sokolova_gs@ya.ru', '89151234567', '4050 123456'))
    cur.execute("REPLACE INTO 'trainings' ('duration','employee_id', 'amount',  'description', 'client_id')  VALUES (?, ?, ?, ?, ?)",
                (1, 0, 12,'бокс',1))
    cur.execute("INSERT INTO 'contracts' ('number', 'date', 'price', 'discount', 'deal_status', 'finish_price', 'training_id', 'client_id', 'employee_id')  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                ('2024-1-ПП', '01.04.2024', 145_000, 3, False, None, 1, 1, 1))

    cur.execute("INSERT INTO 'clients' ('name', 'email', 'phone_number', 'passport')  VALUES (?, ?, ?, ?)",
                ('Михайлов Владимир Степанович', 'mvs2020@ya.ru', '89170001234', '4050 001002'))
    cur.execute("REPLACE INTO 'trainings' ('duration','employee_id', 'amount',  'description', 'client_id')  VALUES (?, ?, ?, ?, ?)", (0, 1, 2, 'гимнастика', 4))
    cur.execute("INSERT  INTO 'contracts' ('number', 'date', 'price', 'discount', 'deal_status', 'finish_price', 'training_id', 'client_id', 'employee_id')  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                ('2024-2-ПП', '04.04.2024',  145_000, 3, False, None, 1, 1, 1))
    connection.commit()
    connection.close()
if __name__ == '__main__':
    init_db()