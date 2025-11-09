from flask import Flask, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
base = Path(__file__).resolve().parents[1]
db = base / 'data' / 'warehouse' / 'supplychain.db'

@app.route('/kpis')
def kpis():
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute('SELECT metric, value FROM kpis')
        rows = cur.fetchall()
        return jsonify([{ 'metric': r[0], 'value': r[1] } for r in rows])
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(port=5001)
