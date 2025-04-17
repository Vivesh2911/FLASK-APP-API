

## 🌐 networking

A basic Flask-based web application to manage and display app information (name, version, description) using SQLite.

---

### 🔧 Features

- Display a list of apps  
- Add new app entries through a web form  
- Uses SQLite as a lightweight database  
- Clean HTML UI with internal CSS

---

### 🧰 Tech Stack

- Python  
- Flask  
- SQLite  
- HTML (with embedded CSS)

---

### 🚀 Getting Started

#### 1. **Clone the Repository**

```bash
git clone https://github.com/your-username/networking.git
cd networking
```

#### 2. **Set Up a Virtual Environment (Recommended)**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

#### 3. **Install Dependencies**

```bash
pip install flask
```

#### 4. **Create the Database**

```bash
sqlite3 apps.db < schema.sql
```

#### 5. **Run the Flask App**

```bash
python app.py
```

Visit: 👉 [http://localhost:5000](http://localhost:5000)

---

### 📁 Project Structure

```
networking/
├── app.py
├── apps.db
├── schema.sql
├── templates/
│   └── index.html
```

---

### 📝 Notes

- Make sure port `5000` is free before running the app.  
- You can change the port in `app.py` if needed:  
  `app.run(port=your_port)`

---

