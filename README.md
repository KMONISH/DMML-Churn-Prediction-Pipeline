# Churn Prediction Pipeline
This repository contains a minimal, runnable skeleton for an end-to-end churn prediction pipeline.
It includes sample data, ingestion, validation, preparation, feature engineering, model training,
and a basic orchestration DAG skeleton.

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

