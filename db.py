import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() # loads all environment variables in the .env file

host = os.getenv("PGHOST")
database = os.getenv("PGDATABASE")
user = os.getenv("PGUSER")
passwd = os.getenv("PGPASSWORD")


class Db():
    """
    Database class
    """
    __conn = None

    def __init__(self):
        self.cursor = None

    def connect(self):
        try:
            self.__conn = psycopg2.connect(
                f"postgresql://{user}:{passwd}@{host}/neondb?sslmode=require&channel_binding=require")
            print("Connected to the database")
            self.cursor = self.__conn.cursor()
        except (Exception, psycopg2.DatabaseError) as err:
            print(f"Error connecting to the database: {err}")
    
    def execute(self, query, *args):
        try:
            if any in args:
                self.cursor.execute(query, tuple(args))
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchall()
        except (psycopg.ProgrammingError):
            print("No result for the query was found")
        return result

    def close(self):
        self.cursor.close()
        self.__conn.close()
        print("Connection closed")