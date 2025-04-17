from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    apps = conn.execute('SELECT * FROM apps').fetchall()  # Fetch all apps from the database
    conn.close()
    return render_template('index.html', apps=apps)

@app.route('/add', methods=['POST'])
def add_app():
    app_name = request.form['app_name']
    version = request.form['version']
    description = request.form['description']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO apps (app_name, version, description) VALUES (?, ?, ?)', 
                 (app_name, version, description))
    conn.commit()
    conn.close()
    
    return 'App added successfully!'

if __name__ == '__main__':
    app.run(debug=True, port=5004)

