# To-do list with Postgres for persistent storage
from db_config import get_connection

conn = get_connection()
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        task VARCHAR(255) NOT NULL,
        done BOOLEAN DEFAULT FALSE
    )
""")
conn.commit()


def add_task(task):
    cur.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    conn.commit()


def view_tasks():
    cur.execute("SELECT id, task, done FROM todos ORDER BY id")
    rows = cur.fetchall()
    if not rows:
        print("No tasks yet.")
    for task_id, task, done in rows:
        status = "[x]" if done else "[ ]"
        print(task_id, status, task)


def complete_task(task_id):
    cur.execute("UPDATE todos SET done = TRUE WHERE id = %s", (task_id,))
    conn.commit()


def delete_task(task_id):
    cur.execute("DELETE FROM todos WHERE id = %s", (task_id,))
    conn.commit()


while True:
    print("\n1. Add task  2. View tasks  3. Complete task  4. Delete task  5. Quit")
    choice = input("Choose: ")
    if choice == "1":
        add_task(input("Task: "))
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task(int(input("Task id: ")))
    elif choice == "4":
        delete_task(int(input("Task id: ")))
    elif choice == "5":
        break
    else:
        print("Invalid choice")

cur.close()
conn.close()
