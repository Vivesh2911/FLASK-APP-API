from flask import Flask, request, jsonify

app = Flask(__name__)
app_db = {}
app_id_counter = 1

@app.route('/add-app', methods=['POST'])
def add_app():
    global app_id_counter
    data = request.json
    if not all(k in data for k in ('app_name', 'version', 'description')):
        return jsonify({'error': 'Missing required fields'}), 400

    app_entry = {
        'id': app_id_counter,
        'app_name': data['app_name'],
        'version': data['version'],
        'description': data['description']
    }

    app_db[app_id_counter] = app_entry
    app_id_counter += 1

    return jsonify({'message': 'App added successfully', 'data': app_entry}), 201

@app.route('/get-app/<int:app_id>', methods=['GET'])
def get_app(app_id):
    app_entry = app_db.get(app_id)
    if not app_entry:
        return jsonify({'error': 'App not found'}), 404
    return jsonify(app_entry), 200
  
@app.route('/')
def home():
    return "Welcome to the Flask App API"


@app.route('/delete-app/<int:app_id>', methods=['DELETE'])
def delete_app(app_id):
    if app_id in app_db:
        deleted_app = app_db.pop(app_id)
        return jsonify({'message': 'App deleted successfully', 'data': deleted_app}), 200
    return jsonify({'error': 'App not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
