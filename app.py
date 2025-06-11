from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# creating users table
def init_db():
    with sqlite3.connect('users.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )''')


@app.route('/')
def home():
    return render_template('codedev.html')


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
 
    with sqlite3.connect('users.db') as conn:
        try:
            conn.execute("INSERT INTO users (first_name,last_name,email,password) VALUES (?, ?, ?, ?)",
                         (first_name, last_name, email, password))
            return render_template('success.html', message=f"thanks for registering, {first_name}!")
        except sqlite3.IntegrityError:
            return "Email already exists. Please log in instead."

    
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
 
    with sqlite3.connect('users.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email= ? AND password=?", (email, password))
        user = cur.fetchone()
        if user:
            return render_template('success.html', message=f"Welcome back, {user[1]}!")
        else:
            return "Invalid credentials."


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
