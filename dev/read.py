import sqlite3 as sql
'''
database = sql.connect("telemetry.db")
cursor = database.cursor()

output = cursor.execute("SELECT * FROM data ORDER BY time DESC LIMIT 1;")

for x in output:
    for i in range(1, 8):
        print(x[i])

'''


binary_string = int("0101110", 2)

print(binary_string)