"""load_to_db.py
Loads sample CSVs into a local SQLite warehouse (data/warehouse/supplychain.db)
"""
import pandas as pd
import sqlite3
from pathlib import Path

base = Path(__file__).resolve().parents[1]
raw = base / 'data' / 'raw'
warehouse = base / 'data' / 'warehouse'
warehouse.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(warehouse / 'supplychain.db')

# Load orders
orders = pd.read_csv(raw / 'orders_sample.csv', parse_dates=['order_placed_at','delivered_at'])
orders.to_sql('orders_raw', conn, if_exists='replace', index=False)

# Load route density
routes = pd.read_csv(raw / 'route_density_sample.csv', parse_dates=['timestamp'])
routes.to_sql('route_density_raw', conn, if_exists='replace', index=False)

print('✅ Loaded raw files into SQLite warehouse:', warehouse / 'supplychain.db')
conn.close()
