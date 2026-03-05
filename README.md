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

###  Data Source

**Wikipedia Recent Changes Stream:**  
`https://stream.wikimedia.org/v2/stream/recentchange`

Event fields:

- `title` – Page title  
- `user` – Editor username  
- `wiki` – Language  
- `timestamp` – Edit time  
- `bot` – Bot indicator  
- `comment` – Edit comment  

---

###  Medallion Architecture

### Bronze Layer
- Stores **raw streaming data**  
- Preserves original JSON payload for debugging  
- Example table: `bronze_wikipedia_events`  
- Notebook: `src/notebooks/bronze_ingestion/`

### Silver Layer
- Cleans & structures data  
- Filters valid edits, normalizes usernames, timestamps, bot flags  
- Example table: `silver_wikipedia_edits`  
- Pipeline: `src/DTLpinline/silver_transformation_dtl_pipeline/`

### Gold Layer
- Analytics-ready tables for dashboards  
- Example metrics:  
  - Top edited pages  
  - Edits per language  
  - Bot vs human edits  
- Notebook: `src/gold/gold_analytics_notebook/`

---


### Technology Stack


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


###  Prerequisites

- Databricks workspace  
- Python 3.x / PySpark  
- Databricks cluster with **Delta Live Tables** enabled  
- Required Python libraries: `sseclient`, `requests`, `pyspark`  
- Access to GitHub for repository clone  

---

###  How to Run the Project

1. **Clone the repository:**

```bash
git clone https://github.com/data-engineer-yogesh/real-time-wikipedia-streaming-pipeline.git
```

2. **Upload notebooks and pipelines to Databricks workspace.**

3. **Install required libraries on the cluster:**
```
%pip install sseclient requests
```
4. **Run the Bronze notebook to start streaming ingestion.**

5. **Deploy DLT pipeline for Silver and Gold transformations.**

6. **Open Databricks SQL dashboard to visualize analytics.**


#### Example Analytics Queries

Most edited pages:

```
SELECT title, COUNT(*) AS edits
FROM silver_wikipedia_edits
GROUP BY title
ORDER BY edits DESC;
```
Edits per language:
```
SELECT wiki, COUNT(*) AS edits
FROM silver_wikipedia_edits
GROUP BY wiki;
```
Bot vs Human edits:
```
SELECT bot, COUNT(*) AS edits
FROM silver_wikipedia_edits
GROUP BY bot;
```

----

### Learning Outcomes
This project demonstrates:

- Real-time streaming ingestion
- Delta Lake & Delta Live Tables pipeline design
- Medallion architecture implementation
- Data transformation best practices
- Analytics-ready dataset creation
- Dashboarding on Databricks

It serves as a portfolio project for data engineering interviews and Databricks certification preparation.

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

