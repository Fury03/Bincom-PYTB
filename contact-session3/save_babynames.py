# Extract baby names with regex (as in session 2) and save them to Postgres
import re
from db_config import get_connection

with open("baby2008.html", "r") as f:
    html = f.read()

rows = re.findall(r"<td>(\d+)</td><td>([A-Za-z]+)</td><td>([A-Za-z]+)</td>", html)

conn = get_connection()
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS babynames (
        id SERIAL PRIMARY KEY,
        year INTEGER,
        rank INTEGER,
        name VARCHAR(50),
        gender VARCHAR(10)
    )
""")

for rank, male, female in rows:
    cur.execute(
        "INSERT INTO babynames (year, rank, name, gender) VALUES (%s, %s, %s, %s)",
        (2008, int(rank), male, "male"),
    )
    cur.execute(
        "INSERT INTO babynames (year, rank, name, gender) VALUES (%s, %s, %s, %s)",
        (2008, int(rank), female, "female"),
    )

conn.commit()
print("Saved", len(rows) * 2, "names")
cur.close()
conn.close()
