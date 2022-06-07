import sqlite3

with sqlite3.connect("../netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            SELECT title, release_year, director
            FROM netflix 
            WHERE director '' AND director IS NOT NULL
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
