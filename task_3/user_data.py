from uuid import uuid4

import psycopg
from psycopg.rows import dict_row

from settings import DatabaseConfig, DATABASE


class UserData:
    """CRUD operations class."""
    def __init__(self, db_config: DatabaseConfig):
        self.db_config = db_config.db_config()

    def create_table(self) -> None:
        """Creates table "USER" with columns FirstName and LastName."""
        with psycopg.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                sql_command = """CREATE TABLE "User" (
                    id serial PRIMARY KEY,
                    uuid varchar UNIQUE NOT NULL,
                    FirstName varchar(50),
                    LastName varchar(50)
                )"""
                cur.execute(sql_command)

    def display_created_table(self) -> list:
        """Returns public tables from database."""
        with psycopg.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                sql_command = """SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'"""
                cur.execute(sql_command)
                data = cur.fetchall()
        return data

    def display_table(self) -> list:
        """Returns all data from "User" table."""
        with psycopg.connect(**self.db_config) as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                sql_command = 'SELECT * FROM "User"'
                cur.execute(sql_command)
                data = cur.fetchall()
        return data

    def insert_user(self, first_name: str, last_name: str) -> dict:
        """Inserts data into "User" table, returns inserted data as dict."""
        with psycopg.connect(**self.db_config) as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                uuid = uuid4().hex
                sql_command = 'INSERT INTO "User" (uuid, FirstName, LastName) VALUES (%s, %s, %s) RETURNING *'
                sql_data = (uuid, first_name, last_name)
                cur.execute(sql_command, sql_data)
                inserted_data = cur.fetchone()
        return inserted_data

    def update_user(self, user_uuid: str, first_name: str, last_name: str) -> dict:
        """Updates data in "User" table by uuid, returns new data as dict."""
        with psycopg.connect(**self.db_config) as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                sql_command = 'UPDATE "User" SET (FirstName, LastName) = (%s, %s) WHERE uuid = %s RETURNING *'
                sql_data = (first_name, last_name, user_uuid)
                cur.execute(sql_command, sql_data)
                updated_data = cur.fetchone()
        return updated_data

    def delete_user(self, user_uuid: str) -> dict:
        """Deletes data from "User" table by uuid, returns deleted data as dict."""
        with psycopg.connect(**self.db_config) as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                sql_command = 'DELETE FROM "User" WHERE uuid = %s RETURNING *'
                sql_data = (user_uuid,)
                cur.execute(sql_command, sql_data)
                deleted_data = cur.fetchone()
        return deleted_data


USER_DB = UserData(DATABASE)
