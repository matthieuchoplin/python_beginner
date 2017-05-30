import sqlite3

first_name, last_name, age = 'John', 'Doe', 21
with sqlite3.connect("test_database.db") as connection:
    for (first_name, last_name, age) in [
        ('John', 'Doe', 21),
        ('John', 'O\'Connor', 21),
        ('Theresa', 'May', 44),
        ('Homer', 'Simpson', 38),
    ]:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO People VALUES"
            "(?, ?, ?)", (first_name, last_name, age))