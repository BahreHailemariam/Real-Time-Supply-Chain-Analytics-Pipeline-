# Power BI Report Spec - Supply Chain Analytics Demo
Pages:
- Logistics Overview: On-time delivery, route performance, delays
- Inventory Performance: stock turnover, reorder alerts
- Supplier Insights: lead time, on-time supplier rate
DAX examples:
OnTimeDelivery% = DIVIDE(CALCULATE(COUNTROWS(Orders), Orders[delay_hours] <= 24), COUNTROWS(Orders))
