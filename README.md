# Traffic Flow Prediction – Data Engineering Project (Part II)

## Project Overview
This project implements a data engineering pipeline for traffic flow prediction using the Metro Interstate Traffic Volume dataset. The pipeline follows ETL principles and includes data ingestion, cleaning, feature engineering, machine learning modeling, and result visualization.

## Dataset
- Dataset Name: Metro Interstate Traffic Volume
- Source: Kaggle / UCI Machine Learning Repository
- Description: Historical traffic volume and weather data collected from interstate highways.

## Research Questions
The project addresses the following research questions, as defined in the approved proposal:

1. How can traffic flow data be ingested, cleaned, and transformed using a structured data engineering pipeline?
2. What temporal and contextual features (such as hour of day and weekday) influence traffic volume patterns?
3. Can a machine learning model be trained on engineered features to predict traffic volume effectively?
4. How does processing data in a structured, pipeline-based workflow support near-real-time or scalable traffic analysis?
5. How can traffic volume predictions and visualizations support data-driven decision-making in traffic management systems?

## Pipeline Description
The data pipeline consists of the following steps:
1. Load raw CSV data
2. Clean missing and invalid values
3. Perform feature engineering
4. Train a machine learning model
5. Generate figures and tables
6. Define task orchestration using an Airflow DAG

## Airflow DAG
An Apache Airflow DAG is included to represent the logical execution order of the pipeline tasks. The DAG is provided for orchestration design purposes only and was not executed as part of this submission.

## Results
- The Linear Regression model achieved a Mean Absolute Error (MAE) of approximately 241 vehicles.
- A traffic volume time-series figure is generated.
- A results table summarizing model performance is included.

## Folder Structure
- `src/`: Python scripts for each stage of the pipeline
- `dags/`: Airflow DAG definition
- `data/`: Dataset files
- `figures/`: Generated figures
- `tables/`: Generated tables

## Tools and Technologies
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Apache Airflow (logical orchestration)

## Author
Name: b.sohilkhan, s.shireen
Course: Data Engineering
