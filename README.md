# Real-Time-Supply-Chain-Analytics-Pipeline-
# 📦 Workflow Specification – Real-Time Supply Chain Analytics Demo

This document provides a comprehensive overview of the **end-to-end pipeline workflow** used in the Real-Time Supply Chain Analytics Demo.  
It explains how raw logistics and ERP data move through ingestion, transformation, storage, analytics, and visualization stages in an automated, real-time system.

---

## **1️⃣ Data Ingestion — Reading CSVs or Simulated Stream Files**

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
