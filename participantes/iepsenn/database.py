import os
from typing import Any
import jinja2
from sqlalchemy import create_engine, text


def create_database_connection():
    db_name = os.environ.get("POSTGRES_DB", "rinha")
    db_user = os.environ.get("POSTGRES_USER", "iepsenn")
    db_pass = os.environ.get("POSTGRES_PASSWORD", "senhasupersegura")
    db_host = os.environ.get("POSTGRES_HOST", "database")
    db_port = os.environ.get("POSTGRES_PORT", "5432")

    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    return create_engine(db_string)


def read_sql_file(filename: str, params: dict = None):
    with open(f"sql/{filename}", "r") as file:
        sql = file.read()

    if not params:
        return sql

    env = jinja2.Environment()
    template = env.from_string(sql)
    return template.render(**params)


def execute_query(db_conn: Any, query: str, has_output: bool = True):
    with db_conn.connect() as conn:
        if has_output:
            return conn.execute(text(query)).all()
        else:
            conn.execute(text(query))
            conn.commit()
