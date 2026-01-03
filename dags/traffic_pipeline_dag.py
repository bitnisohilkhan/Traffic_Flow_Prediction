import multiprocessing
multiprocessing.set_start_method("spawn", force=True)


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# -------------------------------------------------------------------
# FIX PYTHON PATH (CRITICAL FOR AIRFLOW)
# -------------------------------------------------------------------
PROJECT_ROOT = "/Users/bitnisohilkhan/Desktop/UE_Studies/DE/Traffic_Flow_Prediction"
sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------------------------
# TASK WRAPPERS (LAZY IMPORTS — BEST PRACTICE)
# -------------------------------------------------------------------
def load_data_task():
    from src.data_ingestion.load_data import load_data
    load_data()

def clean_data_task():
    from src.data_cleaning.clean_data import clean_data
    clean_data()

def build_features_task():
    from src.feature_engineering.build_features import build_features
    build_features()

def train_model_task():
    from src.modeling.train_model import train_model
    train_model()

def generate_figure_task():
    from src.evaluation.generate_figures_tables import generate_figure
    generate_figure()

# -------------------------------------------------------------------
# DAG DEFINITION
# -------------------------------------------------------------------
with DAG(
    dag_id="traffic_flow_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["traffic", "ml", "data-engineering"],
) as dag:

    task_load = PythonOperator(
        task_id="load_data",
        python_callable=load_data_task,
    )

    task_clean = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data_task,
    )

    task_features = PythonOperator(
        task_id="build_features",
        python_callable=build_features_task,
    )

    task_train = PythonOperator(
        task_id="train_model",
        python_callable=train_model_task,
    )

    task_figure = PythonOperator(
        task_id="generate_figure",
        python_callable=generate_figure_task,
    )

    # Task dependencies
    task_load >> task_clean >> task_features >> task_train >> task_figure
