# Run this once to create the database and the todos table.
# Safe to run again: it skips anything that already exists.
import psycopg2
import db_config

# 1. Create the database (connect to the default "postgres" db first)
conn = psycopg2.connect(
    dbname="postgres",
    user=db_config.DB_USER,
    password=db_config.DB_PASSWORD,
    host=db_config.DB_HOST,
    port=db_config.DB_PORT,
)
conn.autocommit = True
cur = conn.cursor()
cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_config.DB_NAME,))
if cur.fetchone():
    print("Database already exists:", db_config.DB_NAME)
else:
    cur.execute("CREATE DATABASE " + db_config.DB_NAME)
    print("Database created:", db_config.DB_NAME)
cur.close()
conn.close()

# 2. Create the todos table inside the new database
conn = db_config.get_connection()
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        task VARCHAR(255) NOT NULL,
        done BOOLEAN DEFAULT FALSE
    )
""")
conn.commit()
print("Table ready: todos")
cur.close()
conn.close()
