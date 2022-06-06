import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            SELECT director, duration 
            FROM netflix 
            WHERE director = 'Cristina Jacob'
            AND duration > 110
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)