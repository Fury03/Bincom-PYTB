# Bincom PYTB – Python Beginners Class Assignments

Assignments for the Bincom Academy Python Beginners class (PYTB-1126), one folder per contact session.

| Folder | Assignment | Files |
|---|---|---|
| `contact-session2` | Read a full name from a text file and split it into first, middle and last name. Print the local file path using `os`. Extract baby names from `baby2008.html` with regex, sort them with bubble sort, and find names with binary search. | `main.py`, `name.txt`, `baby2008.html` |
| `contact-session3` | Fibonacci series generator. To-do list with Postgres storage. Create a Postgres database and tables and run CRUD operations. Save the extracted baby names to a Postgres table. | `fibonacci.py`, `todo.py`, `crud.py`, `create_database.py`, `save_babynames.py`, `db_config.py` |
| `contact-session4` | Read a csv file (`student_scores.csv`) and run linear regression on the data (slope, intercept, R²). | `regression.py`, `student_scores.csv` |
| `contact-session5` | Multimedia website built with Django: upload and view images, audio and video. | `multimedia_site/` |
| `contact-session6` | Host the multimedia website on GitHub and deploy it to Heroku. | `README.txt` (steps), deployment files in `contact-session5/multimedia_site/` |
| `contact-session7` | Post-training test: Fibonacci generator and a Python/Postgres to-do list. | `fibonacci.py`, `todo.py`, `db_config.py` |

## Running

- Session 2 and 4: `python3 main.py` / `python3 regression.py student_scores.csv`
- Session 3 and 7: install `psycopg2-binary`, set your Postgres details in `db_config.py`, create the database (`create_database.py`), then run the scripts.
- Session 5: see `contact-session5/README.txt`.
