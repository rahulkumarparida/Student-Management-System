import psycopg2
import os
import private
 

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

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


cursor.execute('''CREATE TABLE IF NOT EXISTS students (id serial PRIMARY KEY,sname VARCHAR(100),age INT,rollno VARCHAR(50),regn INT,dept_id INT REFERENCES department(id) );''')
print("Table Created")
cursor.execute('''INSERT INTO students (id, sname, age, rollno, regn, dept_id) VALUES(7, 'Rony Rathore', 20, 'CS-23-51', 23095, 1),(8, 'Rohit Nanda', 21, 'CS-23-52', 23096, 2),(9, 'Anusha Patra', 19, 'CS-23-53', 23097, 1),(10, 'Amit Kumar', 22, 'CS-23-54', 23098, 3); ''')
print('Data added sucessfully')

conn.commit()
conn.close()