# Repository Overview: Healthcare Analytics Pipeline

This repository, `veloukarthik-iitj/capstone-project`, is a healthcare analytics pipeline designed to process and analyze hospital data, specifically focusing on diabetes readmission.

---

## Purpose and Overview

The project uses the **UCI Diabetes 130-US Hospitals dataset** to analyze patient data, clean it, engineer features, and build a machine learning model for predicting hospital readmissions within 30 days.

### **Project Workflow**
1. **Data Ingestion**
2. **Data Cleaning**
3. **Feature Engineering**
4. **Visualization**
5. **Model Training**

---

## Key Components

### 1. **`src/ingest.py`**
- **Purpose**: Ingests raw CSV files and converts them to Parquet format for faster processing.
- **Main Functionality**:
  - Reads data from CSV.
  - Replaces placeholder missing values (e.g., `?`) with `pd.NA`.
  - Saves the processed data as a Parquet file.

---

### 2. **`src/clean.py`**
- **Purpose**: Provides data cleaning and preprocessing functions for the dataset.
- **Functions**:
  - **`load_parquet`**: Loads data from a Parquet file into a Pandas DataFrame.
  - **`drop_identifiers`**: Removes sensitive identifiers like `encounter_id` and `patient_nbr`.
  - **`standardize_missing`**: Replaces empty strings with `pd.NA`.
  - **`encode_target`**: Converts the `readmitted` column into binary values (1 for `<30` days, 0 otherwise).
  - **`basic_impute`**: Fills missing values in columns like `race`, `payer_code`, and `medical_specialty`.
  - **`filter_low_variance`**: Removes columns with low variance based on a threshold.
  - **`save_clean`**: Saves the cleaned data to a Parquet file.

---

### 3. **`src/features.py`**
- **Purpose**: Contains feature engineering utilities.
- **Functions**:
  - **`create_age_group`**: Categorizes patients into age brackets (e.g., `<30`, `30-50`).
  - **`count_comorbidities`**: Calculates the number of comorbidities for each patient.

---

### 4. **`src/etl.py`**
- **Purpose**: Implements the ETL (Extract, Transform, Load) pipeline.
- **Workflow**:
  - Ingest raw data using `ingest.py`.
  - Clean the data using `clean.py`.
  - Perform feature engineering using `features.py`.
  - Save the transformed data.

---

### 5. **`src/visualize.py`**
- **Purpose**: Provides minimal visualization utilities.
- **Functionality**:
  - **`plot_readmission_distribution`**: Plots the distribution of the `readmitted` column.

---

### 6. **`src/model.py`**
- **Purpose**: Trains a baseline Random Forest model to predict readmissions.
- **Steps**:
  - Splits the data into training and testing sets.
  - Trains a Random Forest Classifier.
  - Evaluates the model using metrics like AUC and classification reports.
  - Saves the trained model to a file.

---

### 7. **`airflow/dag_etl.py`**
- **Purpose**: Defines an Airflow DAG for scheduling the ETL pipeline.
- **Tasks**:
  - `ingest`: Runs data ingestion.
  - `clean`: Cleans the data.

---

### 8. **`README.md`**
- **Description**:
  - Provides setup instructions (e.g., virtual environment, dependency installation).
  - Includes commands for running the ETL pipeline and model training.

---

### 9. **`docs/data_dictionary.md`**
- **Purpose**: Documents the dataset fields.
- **Example Fields**:
  - `age`: Age bracket of patients (e.g., `[70-80)`).
  - `race`: Patient's race.
  - `gender`: Patient's gender.
  - `readmitted`: Target variable indicating readmissions (<30 days = 1, otherwise 0).

---

### 10. **Notebook (`notebooks/01-eda.ipynb`)**
- Placeholder for exploratory data analysis (EDA). Currently, the content is empty.

---

## Summary of the Pipeline

1. **Data Ingestion**: Converts raw CSV data to Parquet format.
2. **Data Cleaning**: Cleans and preprocesses the data.
3. **Feature Engineering**: Creates additional derived features.
4. **Visualization**: Provides insights into the data.
5. **Model Training**: Builds and evaluates a predictive model.

This is a modular and extensible project, allowing for easy customization and updates.
