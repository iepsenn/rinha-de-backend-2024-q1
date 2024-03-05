import sqlite3
import jinja2


def execute_ddl_scripts():
    con = create_database_connection()

    initial_clients = [
        (1, 100000, 0),
        (2, 80000, 0),
        (3, 1000000, 0),
        (4, 10000000, 0),
        (5, 500000, 0),
    ]

    cur = con.cursor()

    sql = read_sql_file(filename="create_clients_table.sql")
    cur.execute(sql)
    con.commit()

    sql = read_sql_file(filename="create_transactions_table.sql")
    cur.execute(sql)
    con.commit()

    cur.executemany("INSERT INTO clients VALUES(?, ?, ?)", initial_clients)
    con.commit()  # Remember to commit the transaction after executing INSERT.

    con.close()


def create_database_connection():
    return sqlite3.connect("local.db", check_same_thread=False)


def read_sql_file(filename: str, params: dict = None):
    with open(f"sql/{filename}", "r") as file:
        sql = file.read()

    if not params:
        return sql

    env = jinja2.Environment()
    template = env.from_string(sql)
    return template.render(**params)
