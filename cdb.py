import pymysql

# Connection parameters
host_name = 'localhost'
user_name = 'root'  # Replace 'your_username' with your MySQL username
user_password = '9347317236'
port = 3306  # Replace 'your_password' with your MySQL password

# Create connection
connection = pymysql.connect(host=host_name, user=user_name, password=user_password)
try:
    # Create cursor
    cursor = connection.cursor()
    
    # SQL statement to create a database
    create_database_sql = "CREATE DATABASE IF NOT EXISTS cv"
    
    # Execute SQL statement
    cursor.execute(create_database_sql)
    
    # Commit changes
    connection.commit()
    print("Database 'cv' created successfully")
finally:
    # Close connection
    connection.close()
