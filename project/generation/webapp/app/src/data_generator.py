# -*- coding: utf-8 -*-
import json
import random
from typing import List

import mysql.connector
from faker import Faker

fake = Faker()
fake


def generate_sql_insert_statement(table_name: str, columns: List[str]) -> str:
    cols = ", ".join(columns)
    values = ", ".join(["%s"] * len(columns))
    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({values})"
    return sql


def generate_user_data(num_users: int, num_companies: int) -> tuple[str, List[tuple]]:
    companies = list(range(1, num_companies + 1))
    data = []
    for i in range(num_companies + num_users):
        company_id = companies[i % num_companies]
        data_definition = {
            "CompanyID": company_id,
            "FirstName": fake.first_name(),
            "LastName": fake.last_name(),
            "UserType": random.randint(1, 4),
            "Country": fake.country(),
            "State": fake.state_abbr(),
        }
        data.append(tuple(data_definition.values()))
    return generate_sql_insert_statement("users", data_definition.keys()), data


def generate_company_data(num_companies: int) -> tuple[str, List[str]]:
    data = []
    for i in range(num_companies):
        data_definition = {
            "Name": fake.company(),
            "Country": fake.country(),
            "State": fake.state_abbr(),
        }
        data.append(tuple(data_definition.values()))
    return generate_sql_insert_statement("companies", data_definition.keys()), data


def generate_location_data(
    num_locations: int, num_companies: int
) -> tuple[str, List[tuple]]:
    companies = list(range(1, num_companies + 1))
    data = []
    for i in range(num_companies + num_locations):
        company_id = companies[i % num_companies]
        data_definition = {
            "CompanyID": company_id,
            "Name": fake.word(),
            "Street": fake.street_address(),
            "Country": fake.country(),
            "State": fake.state_abbr(),
            "PostalCode": fake.postcode(),
        }
        data.append(tuple(data_definition.values()))
    return generate_sql_insert_statement("locations", data_definition.keys()), data


def generate_product_data(num_products: int) -> tuple[str, List[str]]:
    data = []
    for _ in range(num_products):
        data_definition = {"Name": fake.color_name(), "Description": fake.sentence()}
        data.append(tuple(data_definition.values()))
    return generate_sql_insert_statement("products", data_definition.keys()), data


def generate_subscription_data(num_locations: int, product_count: int = 5) -> List[str]:
    locations = list(range(1, num_locations + 1))
    data = []
    for i in range(num_locations):
        products: list = []
        for j in range(1, random.randint(1, product_count)):
            product = {
                "ProductID": j,
                "CreationTimestamp": fake.date_time_between(
                    start_date="-1y", end_date="now"
                ).strftime("%Y-%m-%d %H:%M:%S"),
            }
            products.append(product)
        data_definition = {
            "LocationID": locations[i % num_locations],
            "Products": json.dumps(products),
        }
        data.append(tuple(data_definition.values()))
    return generate_sql_insert_statement("subscriptions", data_definition.keys()), data


def insert_data(
    conn: mysql.connector.connection.MySQLConnection,
    insert_query: str,
    data: list[tuple],
    batch_size=1000,
) -> None:

    cursor = conn.cursor()
    with conn.cursor() as cursor:
        for i in range(0, len(data), batch_size):
            batch_data = data[i : i + batch_size]
            cursor.executemany(insert_query, batch_data)
        conn.commit()

    cursor.close()


def reset_table(conn: mysql.connector.connection.MySQLConnection, file: str) -> None:
    with open(file=file) as f:
        sql = f.read()
        cursor = conn.cursor()
        for statement in sql.split(";"):
            if statement.strip() != "":
                cursor.execute(statement)
        conn.commit()
        cursor.close()


def main() -> None:
    conn = mysql.connector.connect(
        host="172.20.0.3", user="data_engineer", password="password", database="webapp"
    )
    reset_table(conn, "./sql/users.sql")
    reset_table(conn, "./sql/companies.sql")
    reset_table(conn, "./sql/locations.sql")
    reset_table(conn, "./sql/subscriptions.sql")
    reset_table(conn, "./sql/products.sql")

    num_companies = 10
    num_users = 5
    num_locations = 5

    insert_data(conn, *generate_company_data(num_companies))
    insert_data(conn, *generate_user_data(num_users, num_companies))
    insert_data(conn, *generate_location_data(num_locations, num_companies))
    insert_data(conn, *generate_subscription_data(num_locations))
    insert_data(conn, *generate_product_data(10))


if __name__ == "__main__":
    main()
