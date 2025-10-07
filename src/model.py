"""Train a baseline model and evaluate performance."""
import argparse
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report

def train_baseline(input_path: str, model_path: str):
    df = pd.read_parquet(input_path)
    if 'readmitted' not in df.columns:
        raise ValueError('readmitted column missing in input')
    y = df['readmitted']
    X = df.select_dtypes(include=['number']).fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    clf.fit(X_train, y_train)
    preds = clf.predict_proba(X_test)[:,1]
    auc = roc_auc_score(y_test, preds)
    print('AUC:', auc)
    y_pred = (preds >= 0.5).astype(int)
    print(classification_report(y_test, y_pred))
    Path = __import__('pathlib').Path
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(clf, model_path)
    print(f'Model saved to {model_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--model-path', required=True)
    args = parser.parse_args()
    train_baseline(args.input, args.model_path)
