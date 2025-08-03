from flask import Flask, render_template, request
import sqlite3, os
from scraper import fetch_case_details

# ✅ Flask App Init
app = Flask(__name__)
DB_PATH = "case_logs.db"

# ✅ Initialize SQLite DB
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_no TEXT,
            year TEXT,
            raw_response TEXT
        )''')
init_db()

# ✅ Save Query Logs
def save_log(case_type, case_no, year, raw_html):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO logs (case_type, case_no, year, raw_response) VALUES (?, ?, ?, ?)",
                     (case_type, case_no, year, raw_html))

# ✅ Home Route
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Search Route
@app.route('/search', methods=['POST'])
def search():
    case_type = request.form['case_type']
    case_no = request.form['case_no']
    year = request.form['year']

    data = fetch_case_details(case_type, case_no, year)
    save_log(case_type, case_no, year, data.get('raw_html', ''))

    return render_template('result.html', details=data) if data['status']=="success" else f"<h3>{data['message']}</h3>"

# ✅ Admin Logs Viewer
@app.route('/logs')
def view_logs():
    with sqlite3.connect(DB_PATH) as conn:
        logs = conn.execute("SELECT id, case_type, case_no, year FROM logs ORDER BY id DESC").fetchall()
    return render_template('logs.html', logs=logs)

# ✅ Render Deployment Compatibility
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
