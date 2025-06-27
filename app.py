import psycopg2
from flask import Flask , redirect , request , render_template , url_for
import private as p 
app = Flask(__name__)

def ConnDb():
    conn = psycopg2.connect(dbname=p.dbname, user=p.user ,password=p.password,host=p.host,port=p.port)
    print('Connection Established')
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
        return render_template('templates/AddStudent.html')



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

        cursor.execute('''UPDATE students SET sname=%s , age=%s , rollno=%s , regn=%s , dept_id=%s  WHERE student_id =%s;''',(name,age,rollno,regn,dept_id,Sid))
        cursor.close()
        conn.commit()
        conn.close()
        return redirect(url_for('index'))    
    elif request.method == 'GET':
        cursor.execute('''SELECT * , department.name AS Dname  FROM students JOIN department ON students.dept_id = department.id WHERE students.student_id = %s;''',(student_id,))
        data = cursor.fetchone()
        print("Updated data FNC:  ",data)
        cursor.close()
        conn.close()
        return render_template('templates/update.html', data=data)
    

@app.route('/deleteUser/<int:student_id>',methods=['GET','POST'])
def delete(student_id):
    conn = ConnDb()
    cursor =conn.cursor()
   
    cursor.execute('''DELETE FROM students WHERE student_id=%s''',(student_id,))
        
    cursor.close()
    conn.commit()
    conn.close()
    return redirect(url_for('index'))    


@app.route('/viewStudent/<int:student_id>', methods=['GET','POST'])
def ViewData(student_id):
    conn = ConnDb()
    cursor = conn.cursor()
    cursor.execute('''SELECT * , department.name AS Dname  FROM students JOIN department ON students.dept_id = department.id WHERE students.student_id = %s;''',(student_id,))
    data = cursor.fetchone()
    print('Viewing ' , data)
    cursor.close()
    conn.commit()
    conn.close()
    return render_template('templates/ViewStudent.html',data = data)

    
    
    
    
    
    
    

    