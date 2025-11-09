"""kpi_calculations.py
Reads cleaned processed CSVs and writes aggregated KPIs into SQLite warehouse tables.
"""
import pandas as pd
import sqlite3
from pathlib import Path

base = Path(__file__).resolve().parents[1]
processed = base / 'data' / 'processed'
warehouse = base / 'data' / 'warehouse'
conn = sqlite3.connect(warehouse / 'supplychain.db')

def compute_kpis():
    files = list(processed.glob('cleaned_*.csv'))
    if not files:
        print('No processed files found. Run transform_data.py first.')
        return
    for f in files:
        df = pd.read_csv(f)
        if 'order_id' in df.columns:
            df.to_sql('orders', conn, if_exists='append', index=False)
        else:
            df.to_sql('routes', conn, if_exists='append', index=False)
    orders = pd.read_sql('SELECT * FROM orders', conn)
    if not orders.empty:
        orders['delay_hours'] = (pd.to_datetime(orders['delivered_at']) - pd.to_datetime(orders['order_placed_at'])).dt.total_seconds()/3600.0
        on_time = (orders['delay_hours'] <= 24).sum()
        total = len(orders)
        on_time_pct = on_time / total if total>0 else None
        kpis = pd.DataFrame([{'metric':'on_time_pct','value':on_time_pct},{'metric':'avg_delivery_hours','value':orders['delay_hours'].mean()}])
        kpis.to_sql('kpis', conn, if_exists='replace', index=False)
        print('KPIs computed and stored in warehouse.kpis')
    else:
        print('No orders to compute KPIs.')

if __name__ == '__main__':
    compute_kpis()
