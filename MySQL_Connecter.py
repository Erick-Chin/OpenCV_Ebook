import MySQL_connecter
import MySQL_connecter import Error


#creating the server takes the host_name, user_name, and user_password
#Starts as a none connetion and it then tries to connect using mysql-connect
def create_server_connection(host_name, user_name, user_password): #used freecodecamp.org how to create and manipulate SQL Databases with Python
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        #Error checking to see if the database connected 
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection



#This is how you would create a database in python for sql
def create_database(connection, query): #This takes a connection and a SQL query 
    cursor = connection.cursor() # The cursor is used to execute SQL queries.
    try:
        cursor.execute(query) #using the curser method to make a curser object using the query 
        print("Database created successfully")#check to see if it worked 
    except Error as err:
        print(f"Error: '{err}'")

#Define a query and call the function 
create_database_query = "CREATE DATABASE school"
create_database (connection, create _database _query)



def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name #takes the database name when connecting to the server 
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection



#Query execution function. It takes the SQL queries stored in python as strings and passes them into the cursor.execute method to execute them on the server 
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit() #makes sure that the commands detailed in the SQL queries are implimented 
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

        