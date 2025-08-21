# Churn Prediction Pipeline
This repository contains a minimal, runnable skeleton for an end-to-end churn prediction pipeline.
It includes sample data, ingestion, validation, preparation, feature engineering, model training,
and a basic orchestration DAG skeleton.

1. Problem Formulation
•	Clearly define the business problem 
•	Identify key business objectives 
•	List the key data sources and their attributes 
•	Define the expected outputs from the pipeline:
o	Clean datasets for exploratory data analysis (EDA)
o	Transformed features for machine learning
o	A deployable model to predict customer churn
•	Set measurable evaluation metrics
•	Deliverables:
o	A PDF/Markdown document with the business problem, objectives, data sources, pipeline outputs, and evaluation metrics.


2. Data Ingestion
•	Identify at least two data sources (e.g., CSV files, REST APIs, database queries)
•	Design scripts for data ingestion, ensuring:
o	Automatic fetching of data periodically (e.g., daily or hourly)
o	Error handling for failed ingestion attempts
o	Logging for monitoring ingestion jobs
•	Deliverables:
o	Python scripts for ingestion (e.g., using pandas, requests etc.)
o	A log file showing successful ingestion runs
o	Screenshots of ingested data stored in raw format

3. Raw Data Storage
•	Store ingested data in a data lake or storage system (e.g., AWS S3, Google Cloud Storage, HDFS, or a local filesystem)
•	Design an efficient folder/bucket structure:
o	Partition data by source, type, and timestamp
•	Deliverables:
o	Folder/bucket structure documentation
o	Python code demonstrating the upload of raw data to the storage system

4. Data Validation
•	Implement data validation checks to ensure data quality:
o	Check for missing or inconsistent data
o	Validate data types, formats, and ranges
o	Identify duplicates or anomalies
•	Generate a comprehensive data quality report
•	Deliverables:
o	A Python script for automated validation (e.g., using pandas, great_expectations, or pydeequ)
o	Sample data quality report in PDF or CSV format, summarizing issues and resolutions

5. Data Preparation
•	Clean and preprocess the raw data:
o	Handle missing values (e.g., imputation or removal)
o	Standardize or normalize numerical attributes
o	Encode categorical variables using one-hot encoding or label encoding
•	Perform EDA to identify trends, distributions, and outliers.
•	Deliverables:
o	Jupyter notebook/Python script showcasing the data preparation process
o	Visualizations and summary statistics (e.g., histograms, box plots)
o	A clean dataset ready for transformations

6. Data Transformation and Storage
•	Perform transformations for feature engineering:
o	Create aggregated features (e.g., total spend per customer)
o	Derive new features (e.g., customer tenure, activity frequency)
o	Scale and normalize features where necessary
•	Store the transformed data in a relational database or a data warehouse.
•	Deliverables:
o	SQL schema design or database setup script
o	Sample queries to retrieve transformed data
o	A summary of the transformation logic applied

7. Feature Store
•	Implement a feature store to manage engineered features:
o	Define metadata for each feature (e.g., description, source, version)
o	Use a feature store tool (e.g., Feast) or a custom solution
•	Automate feature retrieval for training and inference
•	Deliverables:
o	Feature store configuration/code
o	Sample API or query demonstrating feature retrieval
o	Documentation of feature metadata and versions

8. Data Versioning
•	Use version control for raw and transformed datasets to ensure reproducibility:
o	Track changes in data using tools like DVC, Git LFS, or a custom tagging system
o	Store version metadata (e.g., source, timestamp, change log)
•	Deliverables:
o	DVC/Git repository showing dataset versions
o	Documentation of the versioning strategy and workflow

9. Model Building
•	Train a machine learning model to predict customer churn using the prepared features:
o	Use a framework like scikit-learn or TensorFlow
o	Experiment with multiple algorithms (e.g., logistic regression, random forest)
o	Evaluate model performance using metrics such as accuracy, precision, recall, and F1 score
•	Save the trained model using a versioning tool (e.g., MLflow)
•	Deliverables:
o	Python script for model training and evaluation
o	Model performance report
o	A versioned, saved model file (e.g., .pkl, .h5)

10. Orchestrating the Data Pipeline
•	Automate the entire pipeline using an orchestration tool (e.g., Apache Airflow, Prefect, or Kubeflow):
o	Define a Directed Acyclic Graph (DAG) for pipeline tasks.
o	Ensure task dependencies are well-defined (e.g., ingestion → validation → preparation).
o	Monitor pipeline runs and handle failures gracefully.
•	Deliverables:
o	Pipeline DAG/script showcasing task automation
o	Screenshots of successful pipeline runs in the orchestration tool
o	Logs or monitoring dashboard screenshots


## How to use (local):
1. Ensure Python 3.8+ is installed.
2. Create a virtualenv and install dependencies listed in `requirements.txt`.
3. ```bash
   pip install -r requirements.txt
4. Run ingestion to load sample raw data:
   ```bash
   python ingestion/ingest_csv.py
   ```
4. Run validation:
   ```bash
   python validation/validate_data.py
   ```
5. Run preparation & feature engineering:
   ```bash
   python preparation/prepare_data.py
   ```
6. Train the model:
   ```bash
   python training/train.py
   ```
7. Run scoring:
   ```bash
   python scoring/score_batch.py
   ```

Files and folders:
- `seed/` - sample CSVs
- `ingestion/` - ingestion scripts
- `validation/` - data validation scripts
- `preparation/` - cleaning & feature engineering
- `training/` - model training & MLflow skeleton
- `scoring/` - batch scoring script
- `orchestration/` - Airflow DAG skeleton
- `docs/` - problem formulation (markdown & pdf)

