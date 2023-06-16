"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv
import os



BASE_PATH = os.path.abspath("north_data")
EMPLOYEES_PATH = os.path.join(BASE_PATH, "employees_data.csv")
CUSTOMERS_PATH = os.path.join(BASE_PATH, "customers_data.csv")
ORDERS_PATH = os.path.join(BASE_PATH, "orders_data.csv")

employees_list = []
with open(EMPLOYEES_PATH, "r", encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    columns = ["employee_id", "first_name", "last_name", "title", "birth_date", "notes"]
    if reader.fieldnames == columns:
        for employee in reader:
            employees_list.append((employee["employee_id"], employee["first_name"], employee["last_name"],
                                   employee["title"], employee["birth_date"], employee["notes"]))
conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="sadyuga2015")
with conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)",
                        employees_list)
        cur.execute("SELECT * FROM employees_data")
        conn.commit()


conn.close()

customers_list = []
with open(CUSTOMERS_PATH, "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    columns = ["customer_id", "company_name", "contact_name"]
    if reader.fieldnames == columns:
        for customer in reader:
            customers_list.append((customer["customer_id"], customer["company_name"], customer["contact_name"]))

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="sadyuga2015")
with conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO customers_data VALUES (%s, %s, %s)",
                        customers_list)

        conn.commit()


conn.close()

orders_list = []
with open(ORDERS_PATH, "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    columns = ["order_id","customer_id","employee_id","order_date","ship_city"]
    if reader.fieldnames == columns:
        for order in reader:
            orders_list.append((order["order_id"], order["customer_id"],order["employee_id"],order["order_date"],order["ship_city"]))

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="sadyuga2015")
with conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO orders_data VALUES (%s, %s, %s,%s, %s)",
                        orders_list)

        conn.commit()

conn.close()