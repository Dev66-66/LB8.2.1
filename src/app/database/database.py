import sqlite3
import os

def init_db():
    conn = sqlite3.connect('tips.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    ''')

    cursor.execute('SELECT COUNT(*) FROM tips')
    if cursor.fetchone()[0] == 0:
        default_tips = [
            "Пейте больше воды!",
            "Сделайте перерыв и потянитесь.",
            "Не откладывайте на завтра то, что можно сделать сегодня.",
            "Позвоните близкому человеку.",
            "Съешьте лягушку с утра! (Сделайте самое сложное дело первым)",
            "Прогуляйтесь 10 минут.",
            "Выключите уведомления на час.",
            "Запишите 3 хорошие вещи, которые случились сегодня.",
            "Глубоко вдохните 5 раз.",
            "Поблагодарите кого-нибудь."
        ]
        for tip in default_tips:
            cursor.execute('INSERT INTO tips (text) VALUES (?)', (tip,))
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('tips.db')
    conn.row_factory = sqlite3.Row
    return conn