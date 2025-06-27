import psycopg2
import os

print("🔧 Running init_db.py on Render...")

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

print("✅ Connected successfully to database.")

cursor = conn.cursor()

# Create department table
cursor.execute('''
CREATE TABLE IF NOT EXISTS department (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    fees INT,
    duration INT DEFAULT 4
);
''')
print("✅ Table 'department' created.")

# Insert department data
cursor.execute('''
INSERT INTO department (name, fees)
VALUES 
    ('Computer Science', 120000),
    ('Mechanical', 110000),
    ('Civil', 100000),
    ('Electrical', 115000)
ON CONFLICT (name) DO NOTHING;
''')
print("✅ Sample departments added.")

# Create students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    sname VARCHAR(100),
    age INT,
    rollno VARCHAR(50),
    regn INT,
    dept_id INT REFERENCES department(id)
);
''')
print("✅ Table 'students' created.")

# Insert student data
cursor.execute('''
INSERT INTO students (id, sname, age, rollno, regn, dept_id)
VALUES
    (7, 'Rony Rathore', 20, 'CS-23-51', 23095, 1),
    (8, 'Rohit Nanda', 21, 'CS-23-52', 23096, 2),
    (9, 'Anusha Patra', 19, 'CS-23-53', 23097, 1),
    (10, 'Amit Kumar', 22, 'CS-23-54', 23098, 3)
ON CONFLICT (id) DO NOTHING;
''')
print("✅ Sample students added.")

conn.commit()
cursor.close()
conn.close()
print("✅ init_db.py finished successfully.")
