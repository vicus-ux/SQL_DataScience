import sqlite3

conn = sqlite3.connect('Tech_Data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tech (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    cost FLOAT,
    amount INTEGER
)
''')

# Обработка и вставка данных

lines = []

with open("Data.txt", 'r', encoding='UTF-8') as file:
    lines = file.readlines()


for line in lines:
    data = line.strip().split(", ")  # Разделение строки по запятым
    

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()