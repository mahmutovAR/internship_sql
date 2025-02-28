from os import getenv

from dotenv import load_dotenv

load_dotenv()


class DatabaseConfig:
    """Class with database configuration."""
    def __init__(self, user, password, dbname, host, port):
        self.user = user
        self.password = password
        self.dbname = dbname
        self.host = host
        self.port = port

    def db_config(self):
        return {'user': self.user,
                'password': self.password,
                'dbname': self.dbname,
                'host': self.host,
                'port': self.port}


DATABASE_USER = getenv('PGSQL_DATABASE_USER')
DATABASE_PASSWORD = getenv('PGSQL_DATABASE_PASSWORD')
DATABASE_NAME = getenv('PGSQL_DATABASE_NAME')
DATABASE_HOST = getenv('PGSQL_DATABASE_HOST')
DATABASE_PORT = getenv('PGSQL_DATABASE_PORT')

DATABASE = DatabaseConfig(DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_HOST, DATABASE_PORT)
