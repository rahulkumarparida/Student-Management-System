import psycopg2
# app.py
import os
import private  # This sets the environment variables

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

# Example: Connecting to PostgreSQL with psycopg2
import psycopg2

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

print("Connected successfully")


cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS department(id serial PRIMARY KEY,name text UNIQUE NOT NULL , fees int , duration int DEFAULT 4);''')
print("Table Created")
cursor.execute('''INSERT INTO  department(name , fees) VALUES ('Computer Science' , 120000) , ('Mechanical' , 110000) , ('Civil', 100000) , ('Electrical' , 115000);''')
print('Data added sucessfully')


conn.commit()
conn.close()