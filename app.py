import psycopg2
import os

from flask import Flask , request , redirect , render_template , url_for      

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


print("Connected successfully")


def ConnDb():
    conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASSWORD,host=DB_HOST,port=DB_PORT)
    print('Connection Established app.py')
    return conn

@app.route('/',methods=['GET'])
def index():
    conn = ConnDb()
    cursor =conn.cursor()
    cursor.execute('''SELECT * , department.name AS Dname  FROM students JOIN department ON students.dept_id = department.id;''')
    data = cursor.fetchall()
    cursor.execute('''SELECT * FROM department;''')
    deptData = cursor.fetchall()
    print(deptData)
    cursor.close()
    conn.close()
    return render_template('templates/index.html', data=data , deptData=deptData)


@app.route('/newStudent',methods=['GET','POST'])
def addStudent():
    conn = ConnDb()
    cursor =conn.cursor()
    if request.method =='GET':
        cursor.execute('''SELECT * FROM department;''')
        data = cursor.fetchall()
        print("Department data FNC:  ",data)
        cursor.close()
        conn.close() 
        return render_template('templates/AddStudent.html',data=data)

    if request.method == 'POST':  
        name = request.form['name']
        age = request.form['age']
        rollno = request.form['rollno']
        regn = request.form['regn']
        dept_id = request.form['dept_id']
        cursor.execute('''INSERT INTO students(sname,age,rollno,regn,dept_id) VALUES (%s,%s,%s,%s,%s)''',(name,age,rollno,regn,dept_id))
        cursor.close()
        conn.commit()
        conn.close()
        return redirect(url_for('index'))


@app.route('/newdept',methods=['GET','POST'])
def addDepartment():
        conn = ConnDb()
        cursor =conn.cursor()
        if request.method == 'POST':  
            name = request.form['name']
            fees = request.form['fees']
            duration = request.form['duration']


            cursor.execute('''INSERT INTO department(name,fees,duration) VALUES (%s,%s,%s)''',(name,fees,duration))
            cursor.close()
            conn.commit()
            conn.close()
            return redirect(url_for('index')) 
        return render_template('templates/AddDept.html')


@app.route('/updateUser/<int:student_id>',methods=['GET','POST'])
def update(student_id):
    conn = ConnDb()
    cursor =conn.cursor()
    if request.method == 'POST':
        Sid = request.form['student_id']    
        name = request.form['name']
        age = request.form['age']
        rollno = request.form['rollno']
        regn = request.form['regn']
        dept_id = request.form['dept_id']

        cursor.execute('''UPDATE students SET sname=%s , age=%s , rollno=%s , regn=%s , dept_id=%s  WHERE id =%s;''',(name,age,rollno,regn,dept_id,Sid))
        cursor.close()
        conn.commit()
        conn.close()
        return redirect(url_for('index'))    
    elif request.method == 'GET':
        cursor.execute('''SELECT * , department.name AS Dname  FROM students JOIN department ON students.dept_id = department.id WHERE students.id = %s;''',(student_id,))
        data = cursor.fetchone()
        print("Updated data FNC:  ",data)
        cursor.close()
        conn.close()
        return render_template('templates/update.html', data=data)
    

@app.route('/deleteUser/<int:student_id>',methods=['GET','POST'])
def delete(student_id):
    conn = ConnDb()
    cursor =conn.cursor()
   
    cursor.execute('''DELETE FROM students WHERE id=%s''',(student_id,))
        
    cursor.close()
    conn.commit()
    conn.close()
    return redirect(url_for('index'))    


@app.route('/viewStudent/<int:student_id>', methods=['GET','POST'])
def ViewData(student_id):
    conn = ConnDb()
    cursor = conn.cursor()
    cursor.execute('''SELECT * , department.name AS Dname  FROM students JOIN department ON students.dept_id = department.id WHERE students.id = %s;''',(student_id,))
    data = cursor.fetchone()
    print('Viewing ' , data)
    cursor.close()
    conn.commit()
    conn.close()
    return render_template('templates/ViewStudent.html',data = data)


@app.route('/updateDept', methods=['GET','POST'])
def updateDept():
    conn = ConnDb()
    cursor = conn.cursor()
    if request.method == 'POST':
        Did = request.form['Did']
        name = request.form['name']
        fees = request.form['fees']
        duration = request.form['duration']
        cursor.execute('''UPDATE department SET name=%s , fees=%s , duration=%s WHERE id =%s;''',(name,fees,duration,Did))
        cursor.close()
        conn.commit()
        conn.close()
        return redirect(url_for('index'))    
    elif request.method == 'GET':
        cursor.execute('''SELECT * FROM department;''')
        Ddata = cursor.fetchall()
        print('fetched data', Ddata)
        cursor.close()
        conn.close()
        return render_template('templates/updateDept.html', data=Ddata)


    
    
    
    
    
    

    