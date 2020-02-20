import psycopg2
from dotenv import load_dotenv
import os
 
load_dotenv() #loads content of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PSSW = os.getenv("DB_PSSW")
DB_HOST = os.getenv("DB_HOST")

print(DB_NAME, DB_USER, DB_PSSW, DB_HOST)
#print(os.environ.get("SECRET MESSAGE"))


### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PSSW, host=DB_HOST)

print("Connection: ", connection)
### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
### An example query
cursor.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result=cursor.fetchall()

print(result)