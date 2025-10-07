"""Local ETL runner: ingest -> clean -> feature -> save"""
import argparse
from pathlib import Path
from src.ingest import ingest_csv
from src.clean import load_parquet, drop_identifiers, standardize_missing, encode_target, basic_impute, filter_low_variance, save_clean
from src.features import create_age_group

def run_etl(input_csv: str, tmp_parquet: str, cleaned_parquet: str):
    ingest_csv(input_csv, tmp_parquet)
    df = load_parquet(tmp_parquet)
    df = drop_identifiers(df)
    df = standardize_missing(df)
    df = encode_target(df)
    df = basic_impute(df)
    df = filter_low_variance(df)
    df = create_age_group(df)
    save_clean(df, cleaned_parquet)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--tmp', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    run_etl(args.input, args.tmp, args.output)
