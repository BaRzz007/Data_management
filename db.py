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
    __cursor = None

    #def __init__(self):
    #    """
    #    Initialize the db object
    #    """
    #    self.cursor = None

    def connect(self):
        """
        connects to the database
        """
        try:
            self.__conn = psycopg2.connect(
                f"postgresql://{user}:{passwd}@{host}/neondb?sslmode=require&channel_binding=require") # connect using a connection screen
            print("Connected to the database")
            self.__cursor = self.__conn.cursor()
        except (Exception, psycopg2.DatabaseError) as err:
            print(f"Error connecting to the database: {err}")
    
    def execute(self, query, *args):
        """
        wraps the execute method of the cursor object
        """
        try:
            if any in args:
                self.__cursor.execute(query, tuple(args))
            else:
                self.__cursor.execute(query)
            result = self.__cursor.fetchall()
        except (psycopg.ProgrammingError):
            print("No result for the query was found")
        return result

    def close(self):
        """
        Closes the connections to the database
        """
        self.__cursor.close()
        self.__conn.close()
        print("Connection closed")