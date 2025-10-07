"""Simple ingestion utility: reads CSV and writes Parquet for faster downstream processing."""
import argparse
import pandas as pd
from pathlib import Path

def ingest_csv(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    # quick normalization of placeholder missing values
    df.replace("?", pd.NA, inplace=True)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"Wrote {len(df)} rows to {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    ingest_csv(args.input, args.output)
