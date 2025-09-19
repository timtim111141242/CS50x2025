from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# 資料庫初始化
def init_db():
    # 確保資料庫檔案存在
    conn = sqlite3.connect('anger_journal.db')
    c = conn.cursor()

    # 檢查表是否存在，如果不存在則創建
    c.execute('''CREATE TABLE IF NOT EXISTS incidents
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date TEXT NOT NULL,
                 title TEXT NOT NULL,
                 description TEXT,
                 severity INTEGER NOT NULL,
                 tags TEXT,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    # 檢查表中是否有數據，如果沒有則插入範例數據
    result = c.execute('SELECT COUNT(*) FROM incidents').fetchone()
    if result[0] == 0:
        # 插入一些範例數據
        sample_data = [
            ('2023-10-15', '忘了紀念日', '完全忘記了我們的交往紀念日', 4, '紀念日,記憶'),
            ('2023-10-10', '玩遊戲沒回消息', '玩了2小時遊戲沒回她消息', 3, '遊戲,溝通'),
            ('2023-10-05', '遲到15分鐘', '約會遲到了15分鐘', 2, '時間管理'),
        ]

        c.executemany('INSERT INTO incidents (date, title, description, severity, tags) VALUES (?, ?, ?, ?, ?)', sample_data)
        print("已插入示例数据")

    conn.commit()
    conn.close()
    print("数据库初始化完成")

def get_db_connection():
    conn = sqlite3.connect('anger_journal.db')
    conn.row_factory = sqlite3.Row
    return conn

# 在應用程式啟動時初始化資料庫
with app.app_context():
    init_db()

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        incidents = conn.execute('SELECT * FROM incidents ORDER BY date DESC').fetchall()
        conn.close()
        return render_template('index.html', incidents=incidents)
    except Exception as e:
        return f"錯誤: {str(e)}"

@app.route('/add', methods=('GET', 'POST'))
def add_incident():
    if request.method == 'POST':
        try:
            date = request.form['date']
            title = request.form['title']
            description = request.form['description']
            severity = int(request.form['severity'])
            tags = request.form['tags']

            conn = get_db_connection()
            conn.execute('INSERT INTO incidents (date, title, description, severity, tags) VALUES (?, ?, ?, ?, ?)',
                         (date, title, description, severity, tags))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        except Exception as e:
            return f"錯誤: {str(e)}"

    # 設定預設日期為今天
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('add_incident.html', today=today)

@app.route('/stats')
def stats():
    try:
        conn = get_db_connection()

        incidents = conn.execute('SELECT * FROM incidents').fetchall()

        total_incidents = len(incidents)

        severity_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for incident in incidents:
            severity_count[incident['severity']] += 1

        tag_count = {}
        for incident in incidents:
            if incident['tags']:
                for tag in incident['tags'].split(','):
                    tag = tag.strip()
                    if tag:
                        tag_count[tag] = tag_count.get(tag, 0) + 1

        conn.close()

        return render_template('stats.html',
                              total_incidents=total_incidents,
                              severity_count=severity_count,
                              tag_count=tag_count)
    except Exception as e:
        return f"錯誤: {str(e)}"

@app.route('/delete/<int:id>')
def delete_incident(id):
    try:
        conn = get_db_connection()
        conn.execute('DELETE FROM incidents WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    except Exception as e:
        return f"錯誤: {str(e)}"

@app.route('/debug/db')
def debug_db():
    """調試路由，顯示資料庫狀態"""
    try:
        conn = get_db_connection()

        # 檢查表是否存在
        tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()

        # 如果incidents表存在，顯示其中的數據
        incidents = []
        if any(table['name'] == 'incidents' for table in tables):
            incidents = conn.execute('SELECT * FROM incidents').fetchall()

        conn.close()

        return render_template('debug_db.html',
                              tables=tables,
                              incidents=incidents)
    except Exception as e:
        return f"錯誤: {str(e)}"

if __name__ == '__main__':
    # 建立必要的資料夾
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    # 運行應用
    app.run(debug=True, host='0.0.0.0', port=5000)
