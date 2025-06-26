
# 🎓 Student Management System

A full-stack (server-rendered) CRUD web application built using **Flask** and **PostgreSQL** that allows you to manage student records and departmental data efficiently.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Jinja2 Templates)
- **Database**: PostgreSQL
- **Others**: psycopg2 (for DB connection), Jinja templating

---

## 🔑 Features

- 🔹 **Add Student**: Enter student details including name, age, roll number, department, and registration number.
- 🔹 **View Students**: List of all students with department names.
- 🔹 **Update Student Info**: Modify student data via dynamic routes using student ID.
- 🔹 **Delete Student**: Remove student records with a single click.
- 🔹 **Add Department**: Add department name, fees, and duration (default is 4 years).
- 🔹 **Relational Mapping**: Each student is linked to a department using foreign keys.

---

### 📁 Folder Structure

<details>
<summary>Click to expand</summary>

```bash
STUDENT MANAGEMENT SYSTEM/
│
├── app.py                     # Main Flask application file
├── init_db.py                 # Script to initialize database and tables
├── private.py                 # Contains DB credentials (excluded from Git)
├── private_template.py        # Template for DB credentials
├── .gitignore                 # Git ignore rules
├── README.md                  # Project description and setup
│
├── env/                       # Virtual environment (excluded from Git)
│
├── static/                    # Static files (CSS, images)
│   ├── css/
│   │   └── index.css
│   └── Images/
│       └── studentIcon.jpg
│
├── templates/                 # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── AddDept.html
│   ├── AddStudent.html
│   ├── update.html
│   └── ViewStudent.html
│
└── __pycache__/               # Python bytecode cache (excluded)
```

</details>



---

## 🔒 Security Notes

- `private.py` contains sensitive PostgreSQL login info and is **excluded from version control** using `.gitignore`.
- A `private_template.py` file is provided so others can configure their local credentials.

---

## 🚀 How to Run This on Your Local Machine

### 1. 🔃 Clone the Repository
```bash
git clone https://github.com/your-username/student-management.git
cd student-management
````

### 2. 💾 Set Up Virtual Environment

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. 📦 Install Dependencies

```bash
pip install flask psycopg2
```

### 4. 🛠️ Set Up PostgreSQL and Database

* Create a PostgreSQL database (e.g. `studentmanagement`)
* Create a table using `init_db.py`:

```bash
python init_db.py
```

### 5. 🔐 Configure DB Credentials

* Copy the template:

```bash
cp private_template.py private.py
```

* Fill in your own PostgreSQL credentials inside `private.py`.

### 6. 🏃 Run the App

```bash
flask run
```

Open your browser and go to:

```
http://127.0.0.1:5000/

```

---

## 👨‍💻 Author

**Rahul Kumar Parida**

* [GitHub](https://github.com/rahulkumarparida)

---

## 📝 License

This project is open source and free to use for educational purposes.


