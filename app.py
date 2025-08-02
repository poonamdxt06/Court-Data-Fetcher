from flask import Flask, render_template, request
import sqlite3
from scraper import fetch_case_details
import os

app = Flask(__name__)
DB_PATH = "case_logs.db"

# ✅ Initialize Database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_type TEXT,
                    case_no TEXT,
                    year TEXT,
                    raw_response TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

# ✅ Save Logs to DB
def save_log(case_type, case_no, year, raw_html):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO logs (case_type, case_no, year, raw_response) VALUES (?, ?, ?, ?)",
              (case_type, case_no, year, raw_html))
    conn.commit()
    conn.close()

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

    # ✅ Save Query to DB
    save_log(case_type, case_no, year, data.get('raw_html', ''))

    if data['status'] == "success":
        return render_template('result.html', details=data)
    else:
        return f"<h3>{data['message']}</h3>"

# ✅ Admin Logs Viewer
@app.route('/logs')
def view_logs():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, case_type, case_no, year FROM logs ORDER BY id DESC")
    logs = c.fetchall()
    conn.close()
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
