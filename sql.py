import sqlite3

# Function to execute SQL query on the SQLite database
def execute_sql_query(sql_query):
    # Connect to the SQLite database
    connection = sqlite3.connect('sample_database.db')
    cursor = connection.cursor()

    try:
        # Execute the SQL query
        cursor.execute(sql_query)
        # Fetch the query results (if needed)
        results = cursor.fetchall()
        return results
    except Exception as e:
        return str(e)
    finally:
        # Close the database connection
        connection.close()
