# 📦 Real-Time Supply Chain Analytics Pipeline

This project demonstrates how to build a real-time analytics pipeline for supply chain operations, integrating live data ingestion, transformation, and dashboard visualization for actionable insights.
It leverages Python, SQL, Apache Kafka, Power BI, and Streamlit to monitor performance metrics such as order fulfillment, logistics delays, inventory turnover, and supplier performance — all in near real-time.

🧭 Project Overview

Modern supply chains generate vast amounts of data from logistics, warehouse management, and procurement systems.
This project builds an end-to-end data analytics pipeline that continuously collects, processes, and visualizes operational data, enabling timely decisions in demand forecasting, shipment tracking, and vendor reliability analysis.

Core Features:

- ⏱️ Real-time data ingestion from multiple sources (IoT sensors, ERP exports, supplier APIs).

- ⚙️ Data transformation and cleaning using Python and SQL.

- 📊 Interactive Power BI dashboard for supply chain KPIs.

- 🚀 Streamlit app for operational insights and alerts.

🔄 Scheduled ETL automation for continuous updates.

##  Workflow Specification – Real-Time Supply Chain Analytics Demo

This document provides a comprehensive overview of the **end-to-end pipeline workflow** used in the Real-Time Supply Chain Analytics Demo.  
It explains how raw logistics and ERP data move through ingestion, transformation, storage, analytics, and visualization stages in an automated, real-time system.

---

### **1️⃣ Data Ingestion — Reading CSVs or Simulated Stream Files**

**Purpose:**  
Collect live or batch data from multiple operational systems such as ERP, WMS, GPS trackers, or supplier APIs.

**Components:**  
- `scripts/data_ingestion.py` simulates real-time streaming by copying sample raw files into `data/stream/`.
- In production, this step connects to:
  - REST APIs (e.g., Shopify, AWS, SAP)
  - Message queues (Kafka, AWS Kinesis, RabbitMQ)
  - Cloud storage (S3, Azure Blob)

**Output:**  
Raw and streaming data files stored in `data/raw/` or `data/stream/` for transformation.

---
### **2️⃣ Transformation — Data Cleaning and Normalization**

**Purpose:**  
Standardize, enrich, and clean incoming data for consistency and reliability.

**Components:**  
- `scripts/transform_data.py` reads new files from `data/stream/`, performs data validation and cleaning, and writes processed results to `data/processed/`.

**Operations:**  
- Convert timestamps (`order_placed_at`, `delivered_at`) to datetime format.  
- Calculate `delivery_hours = (delivered_at - order_placed_at)`.  
- Normalize SKU formats (e.g., `SKU-001`).  
- Remove duplicates and handle null or inconsistent values.

**Output:**  
Clean and analysis-ready datasets in `data/processed/`.

---
### **3️⃣ Load to Warehouse and Database Loading — Structured Storage**

**Purpose:**  
Store processed data into a structured database (SQLite for demo; can scale to Snowflake, BigQuery, or PostgreSQL).

**Components:**  
- `scripts/load_to_db.py` — performs initial data load.  
- `scripts/kpi_calculations.py` — updates analytics tables with cleaned data.

**Database Schema:**  
| Table | Description |
|--------|-------------|
| `orders_raw` | Original ERP order data |
| `route_density_raw` | Raw GPS route data |
| `orders` | Cleaned and normalized order records |
| `routes` | Enriched vehicle route data |
| `kpis` | Computed KPI results |

**Output:**  
A central SQLite warehouse stored in `data/warehouse/supplychain.db` for analytics and reporting.

---

### **4️⃣ KPI Calculations & Analytics Layer — Business Metrics Generation**

**Purpose:**  
Derive operational insights and key performance metrics from the stored data.

**Components:**  
- `scripts/kpi_calculations.py` computes KPIs and stores results in `kpis` table.  
- `scripts/kpi_api.py` (optional) exposes these KPIs as a JSON API endpoint for external dashboards.

**Example Metrics:**  
| KPI | Definition |
|------|-------------|
| **On-Time Delivery %** | (# Deliveries completed within 24 hours) / (Total Deliveries) |
| **Avg Delivery Time (hrs)** | Mean of `delivery_hours` |
| **Route Efficiency** | Avg stops per vehicle route |
| **Stock Turnover** | (Total Sales) / (Avg Inventory) |

**Output:**  
KPI metrics available for dashboards and automated reports.

---

### **5️⃣ Visualization & Monitoring — Real-Time Insights**

**Purpose:**  
Deliver real-time dashboards for supply chain monitoring and decision-making.

**Components:**  
- **Streamlit App (`scripts/streamlit_app.py`)** — displays live KPIs, trends, and order summaries.  
- **Power BI Dashboard (`dashboard/PowerBI_Report_Spec.md`)** — includes DAX measures and visual layouts.

**Dashboard Pages:**  
| Page | Focus | Visuals |
|-------|--------|----------|
| Logistics Overview | Delivery time, on-time %, delay trends | Bar & Line Charts |
| Inventory Health | Stock turnover, reorder alerts | KPI Cards |
| Supplier Insights | Lead times, reliability | Scatter Plots |
| Operational Costs | Freight cost, route efficiency | Matrix Tables |
| Alerts | SLA breaches, real-time warnings | Color Indicators |

**Output:**  
Dynamic visualization layer powered by both Streamlit and Power BI.

---

### **6️⃣ Automation — Scheduled ETL and Continuous Updates**

**Purpose:**  
Ensure that ingestion, transformation, and KPI computation run automatically on a recurring schedule.

**Components:**  
- `scripts/automate_etl.py` — automates pipeline using Python’s `schedule` library.  
- Can be scaled up using **Apache Airflow** or **AWS Lambda** for enterprise use.

**Example Schedule Code:**  
```python
import schedule, time
from automate_etl import run_etl

schedule.every(30).seconds.do(run_etl)
while True:
    schedule.run_pending()
    time.sleep(1)
```

**Output:**  
ETL and KPIs refresh continuously without manual intervention.

---

### **7️⃣ Notifications & Alerts (Optional Enhancements)**

- Slack or Email alerts for KPI deviations (e.g., on-time delivery < 90%).  
- Integration with Power Automate or Teams for incident escalation.  
- Predictive modeling extensions using Prophet or ARIMA for forecasting.

---

### **🚀 Summary Table**

| Stage | Key Script | Output |
|--------|-------------|---------|
| **1. Ingestion** | `data_ingestion.py` | Simulated real-time data stream |
| **2. Transformation** | `transform_data.py` | Cleaned CSVs (`data/processed/`) |
| **3. Warehouse Loading** | `load_to_db.py`, `kpi_calculations.py` | SQLite data tables |
| **4. KPI Analytics** | `kpi_calculations.py`, `kpi_api.py` | KPI metrics in DB |
| **5. Visualization** | `streamlit_app.py`, Power BI | Real-time dashboards |
| **6. Automation** | `automate_etl.py` | Continuous refresh loop |
| **7. Notifications** | Optional Alerts | Exception-based triggers |
