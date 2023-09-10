#Database module
#Install modules
import psycopg2


# Connect to an existing database
conn = psycopg2.connect(
    dbname="dcrm", user="postgres", password="T4cotote", host="localhost"
    )

# Open a cursor to perform database operations 
cur = conn.cursor()
conn.autocommit = True

cur.execute("CREATE DATABASE eldercode")

print("All Done!")