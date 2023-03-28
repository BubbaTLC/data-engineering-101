from faker import Faker
import random
from typing import List
import mysql.connector

fake = Faker()


def generate_user_data(num_users) -> List[str]:
    sql_statements = []
    for i in range(num_users):
        user_id = i + 1
        company_id = random.randint(1, 10)
        first_name = fake.first_name()
        last_name = fake.last_name()
        user_type = random.randint(0, 4)
        country = fake.country()
        state = fake.state_abbr()
        creation_timestamp = fake \
            .date_time_between(start_date='-1y', end_date='now') \
            .strftime('%Y-%m-%d %H:%M:%S')
        modified_timestamp = creation_timestamp
        # deleted_timestamp = None
        sql = f"""
INSERT INTO users (
    UserID,
    CompanyID,
    FirstName,
    LastName,
    UserType,
    Country,
    State,
    CreationTimestamp,
    ModifiedTimestamp
) VALUES (
    {user_id},
    {company_id},
    '{first_name}',
    '{last_name}',
    {user_type},
    '{country}',
    '{state}',
    '{creation_timestamp}',
    '{modified_timestamp}'
);
"""
        sql_statements.append(sql)
    return sql_statements


def insert_user_data(conn: mysql.connector.connection.MySQLConnection, num_users: int) -> None:
    cursor = conn.cursor()

    # Generate the user data and insert it into the table
    user_data = generate_user_data(num_users)
    for sql_statement in user_data:
        cursor.execute(sql_statement)
    conn.commit()

    cursor.close()


def main() -> None:
    conn = mysql.connector.connect(
        host='172.20.0.3',
        user='data_engineer',
        password='password',
        database='webapp'
    )
    insert_user_data(conn, 10)


if __name__ == '__main__':
    main()
