import psycopg2
import private as p

conn = psycopg2.connect(dbname=p.dbname, user=p.user ,password=p.password,host=p.host,port=p.port)
print('Connection Established')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS department(id serial PRIMARY KEY,name text UNIQUE NOT NULL , fees int , duration int DEFAULT 4);''')
print("Table Created")
cursor.execute('''INSERT INTO  department(name , fees) VALUES ('Computer Science' , 120000) , ('Mechanical' , 110000) , ('Civil', 100000) , ('Electrical' , 115000);''')
print('Data added sucessfully')


conn.commit()
conn.close()