"""Cleaning and preprocessing functions for the diabetes dataset."""
import pandas as pd
import numpy as np
from pathlib import Path

def load_parquet(path: str) -> pd.DataFrame:
    return pd.read_parquet(path)

def drop_identifiers(df: pd.DataFrame) -> pd.DataFrame:
    to_drop = ['encounter_id', 'patient_nbr']
    for c in to_drop:
        if c in df.columns:
            df = df.drop(columns=c)
    return df

def standardize_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.replace("", pd.NA)

def encode_target(df: pd.DataFrame, target_col: str = 'readmitted') -> pd.DataFrame:
    df = df.copy()
    df[target_col] = df[target_col].apply(lambda x: 1 if x == '<30' else 0)
    return df

def basic_impute(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if 'race' in df.columns:
        df['race'] = df['race'].fillna('Unknown')
    for col in ['payer_code', 'medical_specialty']:
        if col in df.columns:
            df[col] = df[col].fillna('Other')
    return df

def filter_low_variance(df: pd.DataFrame, threshold: float = 0.98) -> pd.DataFrame:
    to_drop = []
    for col in df.columns:
        try:
            top_pct = df[col].value_counts(normalize=True, dropna=False).iloc[0]
        except Exception:
            continue
        if top_pct >= threshold:
            to_drop.append(col)
    return df.drop(columns=to_drop)

def save_clean(df: pd.DataFrame, path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    print(f"Saved cleaned data to {path}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    df = load_parquet(args.input)
    df = drop_identifiers(df)
    df = standardize_missing(df)
    df = encode_target(df)
    df = basic_impute(df)
    df = filter_low_variance(df)
    save_clean(df, args.output)
