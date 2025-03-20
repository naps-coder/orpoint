import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "admin",
        password = "admin",
        database = "orpoint"
    )

#cnx = get_db_connection()

#def main ():
#    if cnx.is_connected():
#        print("Connected to MySQL database")
#    else:
#        print("Connection failed")

#main()