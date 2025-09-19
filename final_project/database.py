from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# 數據庫初始化
def init_db():
    # 確保數據庫文件存在
    if not os.path.exists('anger_journal.db'):
        conn = sqlite3.connect('anger_journal.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE incidents
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     date TEXT NOT NULL,
                     title TEXT NOT NULL,
                     description TEXT,
                     severity INTEGER NOT NULL,
                     tags TEXT,
                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        conn.commit()
        conn.close()
        print("數據庫已創建")
    else:
        print("數據庫已存在")

def get_db_connection():
    conn = sqlite3.connect('anger_journal.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        incidents = conn.execute('SELECT * FROM incidents ORDER BY date DESC').fetchall()
        conn.close()
        return render_template('index.html', incidents=incidents)
    except Exception as e:
        return f"錯誤: {str(e)}"

# 其他路由保持不變...

if __name__ == '__main__':
    # 創建必要的文件夾
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    # 初始化數據庫
    init_db()

    # 運行應用
    app.run(debug=True, host='0.0.0.0', port=5000)
