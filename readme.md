# 🚀 **Adzuna Job Data ETL Pipeline**  

## 📌 **About the Project**  

The **Adzuna Job Data ETL Pipeline** is an automated **ETL (Extract, Transform, Load) workflow** designed to collect job postings from the **Adzuna API**, process and transform the data using **AWS Glue**, and store it in **Amazon S3** for further analysis using **Amazon Athena**. The system is fully serverless, leveraging **AWS Lambda, Step Functions, and EventBridge** to ensure scalability, cost-efficiency, and automation.  

This pipeline is designed for businesses, researchers, and analysts who need structured, up-to-date job market data for analytics, reporting, and decision-making.  

---

## 🔄 **Workflow of the Project**  

This ETL pipeline follows a structured workflow using AWS cloud services. Below is a step-by-step breakdown of how the system works: 

---
![Adzuna](https://github.com/shivatadha/Adzuna-Job-Data-ETL-Pipeline/blob/c90b8faa310c259bfef321969dd366bfbbd76dc3/adzuna.png)

---

1️⃣ **Event Trigger:**  
   - **AWS EventBridge** is configured to trigger the pipeline at a scheduled time (e.g., daily).  
   - The event initiates an **AWS Step Function** workflow.  

2️⃣ **Data Extraction (AWS Lambda):**  
   - The **Lambda function** is triggered by Step Functions to fetch job postings from the **Adzuna API**.  
   - The retrieved job postings are stored as raw **JSON files** in an **Amazon S3 bucket**.  

3️⃣ **Data Transformation (AWS Glue & PySpark):**  
   - AWS Glue reads the raw JSON data from S3.  
   - The data is processed using **PySpark** to clean, normalize, and format it.  
   - Transformed data is stored in a separate S3 bucket in **Parquet format**.  

4️⃣ **Schema Inference & Data Catalog (AWS Glue Crawler):**  
   - An **AWS Glue Crawler** scans the transformed data and infers the schema.  
   - The schema is updated in the **AWS Glue Data Catalog**, making the data queryable.  

5️⃣ **Data Analysis (Amazon Athena):**  
   - **Amazon Athena** is used to run **SQL queries** on the processed data.  
   - The structured job data can be analyzed, visualized, or integrated with BI tools like **Amazon QuickSight**.  

---

## 🌟 **Key Features**  

✔️ **Automated job data extraction from Adzuna API**  
✔️ **Serverless & scalable architecture using AWS**  
✔️ **Data transformation using AWS Glue & PySpark**  
✔️ **Schema inference with AWS Glue Crawler**  
✔️ **Querying capabilities via Amazon Athena**  
✔️ **Scheduled execution using AWS EventBridge**  
✔️ **Cost-efficient and highly available infrastructure**  

---

## 🏗 **Module Breakdown**  

🔹 **Data Extraction (AWS Lambda):**  
   - Fetches job postings from the **Adzuna API**.  
   - Handles API authentication and request handling.  
   - Saves raw JSON data to an **S3 bucket**.  

🔹 **Data Transformation (AWS Glue & PySpark):**  
   - Reads raw data from **S3**.  
   - Performs **data cleaning, formatting, and transformation**.  
   - Extracts and normalizes fields like job title, company name, salary, location, and posting date.  
   - Writes transformed data to **S3** in **Parquet format**.  

🔹 **Data Storage (Amazon S3):**  
   - Stores **raw JSON** and **transformed Parquet files**.  
   - Ensures **data durability and security**.  

🔹 **Schema Inference & Data Catalog (AWS Glue Crawler):**  
   - Scans transformed Parquet files in **S3**.  
   - Automatically **infers schema** and updates the AWS Glue **Data Catalog**.  

🔹 **Data Analysis (Amazon Athena):**  
   - Enables querying of structured job data using **SQL-like syntax**.  
   - Allows integration with **BI tools** like QuickSight, Tableau, or Power BI.  

---

## 💻 **Tech Stack & AWS Services Used**  

🟢 **AWS Services:**  
   - **AWS Lambda** → Serverless data extraction  
   - **AWS Step Functions** → Workflow orchestration  
   - **AWS Glue** → ETL processing & data transformation  
   - **AWS Glue Crawler** → Schema inference & Data Catalog  
   - **Amazon S3** → Cloud storage for raw & transformed data  
   - **Amazon Athena** → SQL-based querying for job data  
   - **AWS EventBridge** → Scheduled job execution  

🟢 **Programming Languages & Frameworks:**  
   - **Python** → AWS Lambda & ETL scripts  
   - **PySpark** → Data transformation in AWS Glue  
   - **Boto3** → AWS SDK for Python (S3, Lambda, Glue, etc.)  

🟢 **Data Formats:**  
   - **JSON** (Raw job data)  
   - **Parquet** (Optimized transformed data)  

---

## ⚙️ **Installation and Setup**  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/shivatadha/adzuna-etl.git
cd adzuna-etl
```

### 2️⃣ **Set Up AWS Environment**  
- Create an **S3 bucket** for raw and transformed job data.  
- Configure **AWS Lambda** function and attach necessary permissions (S3 read/write, API Gateway access).  
- Set up **AWS Glue Job** and **Glue Crawler**.  

### 3️⃣ **Deploy Lambda Function for Data Extraction**  
- Navigate to AWS Lambda and create a new function.  
- Upload the `data_extraction.py` script.  
- Set environment variables:  
  ```bash
  ADZUNA_APP_ID = "your-app-id"
  ADZUNA_APP_KEY = "your-app-key"
  S3_BUCKET_NAME = "your-s3-bucket"
  S3_FOLDER = "raw_data"
  ```

### 4️⃣ **Set Up AWS Glue for Data Transformation**  
- Navigate to AWS Glue and create a new **ETL job**.  
- Upload and configure `data_transformation.py`.  
- Define source S3 path (`s3://your-bucket/raw_data/`) and target S3 path (`s3://your-bucket/transformed_data/`).  

### 5️⃣ **Run the Pipeline**  
- Manually trigger AWS Step Functions or schedule it using AWS EventBridge.  
- Check **S3 buckets** to verify raw and transformed data storage.  
- Use **Amazon Athena** to run queries on processed data.  

---

## 🚀 **Future Improvements**  

🔸 **Real-time streaming:** Implement **AWS Kinesis** for real-time data ingestion.  
🔸 **Data enrichment:** Integrate additional APIs (e.g., salary trends, company reviews).  
🔸 **Data visualization:** Build a **dashboard** using **Amazon QuickSight**.  
🔸 **Machine learning:** Apply **ML models** for job market predictions.  

---

## 🏁 **Conclusion**  

This **serverless ETL pipeline** provides a robust solution for extracting, processing, and analyzing job market data using AWS. With its **scalable and automated** design, it can efficiently handle **large volumes of job postings** while enabling advanced **data analysis and visualization**.  

