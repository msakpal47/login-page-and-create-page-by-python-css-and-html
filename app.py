from flask import Flask, render_template, request, redirect, session
import pyodbc



app = Flask(__name__)
app.secret_key = 'your_secret_key'

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"  # Note the double backslash
    "Database=Godrej_Boys;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
cursor = conn.cursor()

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = account[2]
            return redirect('/dashboard')
        else:
            msg = 'Incorrect Username/Password!'
    return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        gender = request.form['gender']

        cursor.execute("INSERT INTO Users (full_name, username, email, phone, password, gender) VALUES (?, ?, ?, ?, ?, ?)",
                       (full_name, username, email, phone, password, gender))
        conn.commit()
        msg = 'You have successfully registered!'
        
        return redirect('/login')
    return render_template('register.html', msg=msg)

@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
