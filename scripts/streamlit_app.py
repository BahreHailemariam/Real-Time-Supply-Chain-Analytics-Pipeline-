"""streamlit_app.py
Streamlit app to visualize KPIs and recent orders from the SQLite warehouse.
Run with: streamlit run scripts/streamlit_app.py
"""
import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.express as px

base = Path(__file__).resolve().parents[1]
warehouse = base / 'data' / 'warehouse' / 'supplychain.db'

st.set_page_config(page_title='Supply Chain Live', layout='wide')
st.title('📦 Real-Time Supply Chain KPIs')

if not warehouse.exists():
    st.warning('Warehouse DB not found. Run load_to_db.py first.')
else:
    conn = sqlite3.connect(warehouse)
    try:
        kpis = pd.read_sql('SELECT * FROM kpis', conn)
        orders = pd.read_sql('SELECT * FROM orders ORDER BY order_placed_at DESC LIMIT 50', conn)
        st.subheader('Key KPIs')
        if not kpis.empty:
            kpi1 = kpis.loc[kpis.metric=='on_time_pct','value'].values[0]
            kpi2 = kpis.loc[kpis.metric=='avg_delivery_hours','value'].values[0]
            st.metric('On-time Delivery %', f"{kpi1:.0%}" if kpi1 is not None else 'N/A')
            st.metric('Avg Delivery Hours', f"{kpi2:.1f}" if kpi2 is not None else 'N/A')
        st.subheader('Recent Orders')
        if not orders.empty:
            orders['order_placed_at'] = pd.to_datetime(orders['order_placed_at'])
            fig = px.bar(orders, x='order_placed_at', y='quantity', color='warehouse', title='Recent Orders Quantity by Time')
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(orders)
        else:
            st.info('No orders in warehouse. Run ETL.')
    finally:
        conn.close()
