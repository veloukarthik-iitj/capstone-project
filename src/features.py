"""Feature engineering utilities."""
import pandas as pd

def create_age_group(df: pd.DataFrame, age_col: str = 'age') -> pd.DataFrame:
    df = df.copy()
    if age_col in df.columns:
        df['age_min'] = df[age_col].str.extract(r"\[(\d+)-")[0].astype(float)
        df['age_group'] = pd.cut(df['age_min'], bins=[0,30,50,70,120], labels=['<30','30-50','50-70','70+'])
        df.drop(columns=['age_min'], inplace=True)
    return df

def count_comorbidities(df: pd.DataFrame, diag_cols_prefix: str = 'diag_') -> pd.DataFrame:
    df = df.copy()
    diag_cols = [c for c in df.columns if c.startswith(diag_cols_prefix)]
    if diag_cols:
        df['comorbidity_count'] = df[diag_cols].notna().sum(axis=1)
    return df
