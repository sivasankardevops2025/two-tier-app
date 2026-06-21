from flask import Flask, render_template, request, redirect
import pymysql, os
 
app = Flask(__name__)
 
def get_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'mysql-service'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME', 'employeedb')
    )
 
@app.route('/')
def index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name, department FROM employees')
    employees = cur.fetchall()
    conn.close()
    return render_template('index.html', employees=employees)
 
@app.route('/add', methods=['POST'])
def add():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO employees (name, department) VALUES (%s, %s)',
                (request.form['name'], request.form['department']))
    conn.commit()
    conn.close()
    return redirect('/')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
