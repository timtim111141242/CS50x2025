from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# 数据库初始化
def init_db():
    # 确保数据库文件存在
    conn = sqlite3.connect('anger_journal.db')
    c = conn.cursor()

    # 检查表是否存在，如果不存在则创建
    c.execute('''CREATE TABLE IF NOT EXISTS incidents
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date TEXT NOT NULL,
                 title TEXT NOT NULL,
                 description TEXT,
                 severity INTEGER NOT NULL,
                 tags TEXT,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    # 检查表中是否有数据，如果没有则插入示例数据
    result = c.execute('SELECT COUNT(*) FROM incidents').fetchone()
    if result[0] == 0:
        # 插入一些示例数据
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

@app.before_first_request
def before_first_request():
    """在第一个请求之前初始化数据库"""
    init_db()

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        incidents = conn.execute('SELECT * FROM incidents ORDER BY date DESC').fetchall()
        conn.close()
        return render_template('index.html', incidents=incidents)
    except Exception as e:
        return f"错误: {str(e)}"

# 其他路由保持不变...

if __name__ == '__main__':
    # 创建必要的文件夹
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    # 初始化数据库
    init_db()

    # 运行应用
    app.run(debug=True, host='0.0.0.0', port=5000)
