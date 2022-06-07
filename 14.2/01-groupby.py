import sqlite3

with sqlite3.connect("../netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            SELECT type
            FROM netflix
            WHERE country != ''
            GROUP BY type
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)