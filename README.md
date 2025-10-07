# Healthcare Analytics Pipeline

Starter codebase for the MediCare Hospital capstone project. Uses the UCI Diabetes 130-US Hospitals dataset.

## Setup

1. Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # mac/linux
.venv\Scripts\activate     # windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Place `diabetic_data.csv` inside `data/`.

4. Run quick local ETL:

```bash
python -m src.etl --input data/diabetic_data.csv --tmp data/tmp/diabetic.parquet --output data/cleaned_diabetes.parquet
```

5. Train a baseline model:

```bash
python -m src.model --input data/cleaned_diabetes.parquet --model-path models/baseline.pkl
```

## Project structure
See repo tree in the root of this README.
