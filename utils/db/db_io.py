import sqlite3
import pandas as pd
import csv


def csv_output_categories():
    db_file = 'data/database.db'
    conn = sqlite3.connect(db_file, isolation_level=None,
                           detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM categories", conn)
    db_df.to_csv('csv_output/dbo_cat.csv', index=False)


def csv_output_products():
    db_file = 'data/database.db'
    conn = sqlite3.connect(db_file, isolation_level=None,
                           detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM products", conn)
    db_df.to_csv('csv_output/dbo_product.csv', index=False)


def csv_input_categories():
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    with open('csv_input/dbi_cat.csv', 'r') as fin:
        # csv.DictReader по умолчанию использует первую строку под заголовки столбцов
        dr = csv.DictReader(fin, delimiter=";")
        to_db = [(i['idx'], i['title'], i['parentID']) for i in dr]

    cur.executemany("INSERT INTO categories (idx, title, parentID) VALUES (?, ?, ?);", to_db)
    con.commit()
    con.close()


def csv_input_products():
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    with open('csv_input/dbi_product.csv', 'r') as fin:
        # csv.DictReader по умолчанию использует первую строку под заголовки столбцов
        dr = csv.DictReader(fin, delimiter=";")
        to_db = [(i['idx'], i['title'], i['body'], i['photo'], i['price'], i['tag']) for i in dr]

    cur.executemany("INSERT INTO products (idx, title, body, photo, price, tag) VALUES (?, ?, ?, ?, ?, ?);", to_db)
    con.commit()
    con.close()
