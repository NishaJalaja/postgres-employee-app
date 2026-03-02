import psycopg2

connection = None
try:
    # 1. Connect to your database
    connection = psycopg2.connect(
        user="dbadmin",
        password="bhagavathi1",
        host="my-test-postgres-db.ch4kq2860gzt.eu-north-1.rds.amazonaws.com",
        port="5432",
        database="test"
    )
    cursor = connection.cursor()

    # 2. Define the SQL and data
    insert_query = """INSERT INTO employee (employeeId, employeename, age, salary) 
                      VALUES (%d, %s, %d, %d)"""
    record_to_insert = (1, 'Alice Smith', 35, 95000)

    # 3. Execute and Commit
    cursor.execute(insert_query, record_to_insert)
    connection.commit()
    
    print("Employee record inserted successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()