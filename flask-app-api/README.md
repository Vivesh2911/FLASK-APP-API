

## ⚡ flash-app-api

A simple Flask-based API to manage and display a list of apps with their name, version, and description.

---

### 🔧 Features

- View existing apps  
- Add a new app through a form  
- Uses SQLite for data storage  

---

### 📦 Technologies Used

- Python  
- Flask  
- SQLite  
- HTML (with internal CSS)

---

### 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/flash-app-api.git
   cd flash-app-api
   ```

2. **Set up a virtual environment (optional):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install flask
   ```

4. **Create the database:**

   ```bash
   sqlite3 apps.db < schema.sql
   ```

5. **Run the Flask app:**

   ```bash
   python app.py
   ```

6. Open your browser and go to:  
   👉 [http://localhost:5000](http://localhost:5000)

---

### 📁 Files

- `app.py` – Main Flask application  
- `apps.db` – SQLite database  
- `schema.sql` – Table creation script  
- `templates/index.html` – HTML template with form  

---

