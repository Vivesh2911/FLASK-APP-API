from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('apps.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.json
    app_name = data.get('app_name')
    version = data.get('version')
    description = data.get('description')

    conn = get_db_connection()
    conn.execute('INSERT INTO apps (app_name, version, description) VALUES (?, ?, ?)',
                 (app_name, version, description))
    conn.commit()
    conn.close()

    return jsonify({'message': 'App added successfully'}), 201

@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    conn = get_db_connection()
    app_data = conn.execute('SELECT * FROM apps WHERE id = ?', (id,)).fetchone()
    conn.close()

    if app_data is None:
        return jsonify({'error': 'App not found'}), 404

    return jsonify(dict(app_data)), 200

@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    conn = get_db_connection()
    result = conn.execute('DELETE FROM apps WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    if result.rowcount == 0:
        return jsonify({'error': 'App not found'}), 404

    return jsonify({'message': 'App deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)

