# Run this once to create the database (connects to the default "postgres" db)
import psycopg2
import db_config

conn = psycopg2.connect(
    dbname="postgres",
    user=db_config.DB_USER,
    password=db_config.DB_PASSWORD,
    host=db_config.DB_HOST,
    port=db_config.DB_PORT,
)
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE " + db_config.DB_NAME)
print("Database created:", db_config.DB_NAME)
cur.close()
conn.close()
