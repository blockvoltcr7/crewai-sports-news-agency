import psycopg2

class PostgresDB:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            return self.connection
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            return None

    def execute_query(self, query):
        if self.connection is None:
            print("No connection to the database")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            for record in records:
                print(record)
        except (Exception, psycopg2.Error) as error:
            print("Error executing query", error)
            
            
    def execute_query_return_cursor(self, query):
        if self.connection is None:
            print("No connection to the database")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Error executing query", error)
            
            
    def get_column_names(self, connection, table_name):
        if self.connection is None:
            print("No connection to the database")
            return

        try:
            cursor = connection.cursor()
            query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';"
            cursor.execute(query)
            column_names = [row[0] for row in cursor.fetchall()]
            for name in column_names:
                print(name)
        except (Exception, psycopg2.Error) as error:
            print("Error executing query", error)