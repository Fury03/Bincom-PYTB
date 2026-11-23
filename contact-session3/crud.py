# CRUD operations on a Postgres table
from db_config import get_connection

conn = get_connection()
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INTEGER
    )
""")
conn.commit()

# CREATE
cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Damilola", 22))
cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Ade", 20))
conn.commit()

# READ
cur.execute("SELECT * FROM students")
print("After insert:", cur.fetchall())

# UPDATE
cur.execute("UPDATE students SET age = %s WHERE name = %s", (23, "Damilola"))
conn.commit()
cur.execute("SELECT * FROM students")
print("After update:", cur.fetchall())

# DELETE
cur.execute("DELETE FROM students WHERE name = %s", ("Ade",))
conn.commit()
cur.execute("SELECT * FROM students")
print("After delete:", cur.fetchall())

cur.close()
conn.close()
