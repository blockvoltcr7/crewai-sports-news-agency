import pytest
import psycopg2
from utilities.postgresql_utils import PostgresDB

def test_postgres_connection():
    try:
        # Replace the following values with your actual database connection details
        connection = psycopg2.connect(
            user="samisabir-idrissi",
            password="localmacm1",
            host="127.0.0.1",
            port="5433",
            database="template1"
        )
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT * from games;")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        pytest.fail("Failed to connect to database")

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
            
def test_postgres_connection_with_credentials():
    # Create an instance of the PostgresDB class
    db = PostgresDB(user="samisabir-idrissi", password="localmacm1", host="127.0.0.1", port="5433", database="template1")

    # Connect to the database
    db.connect()

    # Execute a query
    db.execute_query("SELECT * from games;")
    
def test_get_all_column_names():
    # Create an instance of the PostgresDB class
    db = PostgresDB(user="samisabir-idrissi", password="localmacm1", host="127.0.0.1", port="5433", database="template1")
    connection = db.connect()
    db.get_column_names(connection,"games")

    
def test_func_return_data_as_dictionary():
    # Create an instance of the PostgresDB class
    db = PostgresDB(user="samisabir-idrissi", password="localmacm1", host="127.0.0.1", port="5433", database="template1")
    conn = db.connect()
    c = conn.cursor()
    team_name = "Bulls"
    c.execute("SELECT * from games WHERE team_name = %s;", (team_name,))
    result = c.fetchone()
    db.get_column_names(conn,"games")
    if result:
        keys = ["team_name", "game_id", "status", "home_team", "home_team_score", "away_team","away_team_score"]
        # game_score = dict(zip(keys, result))
        # print(f'game score: {game_score}')
        data = dict(zip(keys, result))
        print(f'data: {data}')
        assert data.get("team_name") == "Bulls"
    else:
        return {'error': 'No game scores found for the team.'}