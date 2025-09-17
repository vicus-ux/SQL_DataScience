import sqlite3

conn = sqlite3.connect('Tech_Data.db')
cursor = conn.cursor()

cursor.execute("SELECT name, category, cost, amount FROM tech WHERE category = 'Ноутбук'")
results = cursor.fetchall()
for i in range(len(results)):
    print(results[i][0], results[i][1], results[i][2], results[i][3])

print()

cursor.execute("SELECT name, cost FROM tech WHERE category = 'Смартфон' AND cost > 50000")
results = cursor.fetchall()
for i in range(len(results)):
    print(results[i][0],results[i][1])

print()

cursor.execute("SELECT name,cost FROM tech ORDER BY cost")
results = cursor.fetchall()
for i in range(len(results)):
    print(results[i][0],results[i][1])


conn.close()

