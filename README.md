# Real-time-wikipedia-streaming-pipeline
A **real-time data engineering project** that ingests live Wikipedia edit events and processes them using **the Databricks Lakehouse Medallion Architecture (Bronze → Silver → Gold).**
The pipeline captures live streaming events from the **Wikipedia Recent Changes API,** processes them using **Spark Structured Streaming**, transforms them using Delta Live Tables (DLT), and visualizes insights in a **Databricks SQL Dashboard.**
This project demonstrates modern data engineering practices used in production environments.

----
### Architecture Overview
<img width="1536" height="1024" alt="Architecture Overview" src="https://github.com/user-attachments/assets/c3d69692-9bb7-4831-b2bf-eb9915dfbd53" />


----

#### Pipeline Flow
```

Wikipedia Live Stream API
        │
        ▼
Bronze Layer (Raw Streaming Data)
        │
        ▼
Silver Layer (Cleaned & Structured Data)
        │
        ▼
Gold Layer (Aggregated Analytics Tables)
        │
        ▼
Databricks SQL Dashboard (Real-Time Insights)
```

#### Project Objectives


This project demonstrates how to build a **modern real-time data pipeline** using the Databricks ecosystem.

Key goals:

- Ingest real-time streaming data
- Implement Medallion Architecture
- Use Delta Live Tables (DLT)
- Apply data cleaning and transformations
- Create analytics-ready datasets
- Build real-time dashboards
- Deploy pipelines using Databricks Asset Bundles

----

Data Source
The pipeline uses the public Wikipedia Event Stream API.
Stream endpoint:
https://stream.wikimedia.org/v2/stream/recentchange

This stream publishes live Wikipedia edit events, including:
- Page edits
- New page creations
- User edits
- Bot edits
- Timestamps
- Page titles

----

##### Technology Stack


| Tool                       | Purpose                        |
| -------------------------- | ------------------------------ |
| Databricks                 | Data engineering platform      |
| Apache Spark               | Distributed processing         |
| Spark Structured Streaming | Real-time streaming            |
| Delta Lake                 | Reliable data storage          |
| Delta Live Tables          | Streaming transformations      |
| Databricks SQL             | Data visualization             |
| Databricks Asset Bundles   | Deployment and version control |
| GitHub                     | Source control                 |

----

```
real-time-wikipedia-streaming-pipeline
│
├── src
│
│   ├── notebooks
│   │
│   │   └── bronze_ingestion
│   │       └── wikipedia_stream_ingestion_notebook
│
│   ├── DTLpinline
│   │
│   │   └── silver_transformation_dtl_pipeline
│
│   ├── gold
│   │
│   │   └── gold_analytics_notebook
│
│   └── dashboard
│       └── wikipedia_dashboard.json
│
├── architecture.png
│
└── README.md
```

----

#### Future Improvements

Potential enhancements:
- Add Kafka as streaming source
- Implement data quality checks
- Add alerting on edit spikes
- Build advanced analytics models
- Integrate with BI tools

---

🪪 License
MIT License — for learning, demonstration, and portfolio purposes.

