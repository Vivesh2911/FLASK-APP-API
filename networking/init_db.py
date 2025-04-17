import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')  # This will create database.db in the same directory
    c = conn.cursor()

    # SQL schema for creating the 'apps' table
    c.execute('''
    CREATE TABLE IF NOT EXISTS apps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_name TEXT NOT NULL,
        version TEXT,
        description TEXT
    );
    ''')

    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
    print("Database and table created successfully!")
