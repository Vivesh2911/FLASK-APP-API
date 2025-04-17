## 📦 database-management-api

A lightweight Flask-based API for managing a simple app database. This project allows users to view and add application entries with details like name, version, and description.

---

### 🚀 Features

- View a list of all apps
- Add new apps using a simple HTML form
- SQLite database integration
- Clean internal CSS for UI styling

---

### 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML with internal CSS
- **Database**: SQLite

---

### 📁 Project Structure

```
database-management-api/
│
├── app.py                 # Main Flask app
├── apps.db                # SQLite database file
├── templates/
│   └── index.html         # HTML template
├── schema.sql             # SQL schema for table creation
└── README.md              # Project documentation
```

---

### ⚙️ Setup Instructions

#### 1. Clone the repo

```bash
git clone https://github.com/your-username/database-management-api.git
cd database-management-api
```

#### 2. Create virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install flask
```

#### 4. Create the database

```bash
sqlite3 apps.db < schema.sql
```

#### 5. Run the server

```bash
python app.py
```

Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 📝 Example App Entry

```json
{
  "app_name": "Spotify",
  "version": "1.1.84",
  "description": "Music streaming application"
}
```

---
