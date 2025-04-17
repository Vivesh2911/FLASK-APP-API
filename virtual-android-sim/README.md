## 📱 virtual-android-sim

A lightweight Flask-based web application that simulates a virtual Android environment for managing apps with basic CRUD functionality.

---

### 🌟 Features

- Simulate app data similar to an Android system  
- Add new apps with version and description  
- View all installed apps  
- Backend powered by Flask and SQLite  
- Easy-to-use HTML interface

---

### ⚙️ Tech Stack

- Python 3  
- Flask  
- SQLite  
- HTML/CSS

---

### 🚀 Getting Started

#### 1. **Clone the Repository**

```bash
git clone https://github.com/your-username/virtual-android-sim.git
cd virtual-android-sim
```

#### 2. **Create a Virtual Environment (Optional but Recommended)**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

#### 3. **Install Dependencies**

```bash
pip install flask
```

#### 4. **Set Up the Database**

```bash
sqlite3 apps.db < schema.sql
```

#### 5. **Run the App**

```bash
python app.py
```

Then open your browser and go to:  
👉 [http://localhost:5000](http://localhost:5000)

---

### 📁 Project Structure

```
virtual-android-sim/
├── app.py
├── apps.db
├── schema.sql
├── templates/
│   └── index.html
```

---

### 📝 Notes

- The app simulates a simplified version of Android app management.  
- Built to demonstrate web-based simulation using Flask.  
- Modify or extend the schema for more complex behaviors.

---

