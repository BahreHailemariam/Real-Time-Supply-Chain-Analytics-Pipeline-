# Workflow Specification - Real-Time Supply Chain Analytics Demo

1. Data Ingestion - read CSVs or simulated stream files
2. Transformation - clean timestamps, calculate delivery time, normalize SKUs
3. Load to Warehouse - write to SQLite tables (orders, routes)
4. KPI Calculations - compute on-time %, delivery times, stock turnover
5. Visualization - Streamlit app reads warehouse and displays KPIs, charts, and alerts
6. Automation - automate ETL loop via schedule or cron
