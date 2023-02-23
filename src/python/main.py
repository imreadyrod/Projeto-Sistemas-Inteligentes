import sqlite3
import pandas as pd
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect("../data/basketball.sqlite")
        return con
    except Error:
        print(Error)


def sql_select_table(con, table: str):
    query = f"SELECT * FROM {table}"
    return pd.read_sql_query(query, con)


table = "News_Missing"
con = sql_connection()
df = sql_select_table(con, table)
df.to_csv(f"../data/{table}.csv")
