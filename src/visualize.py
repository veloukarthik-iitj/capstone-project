"""Minimal visualization helpers."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_readmission_distribution(df: pd.DataFrame, save_path: str = None):
    plt.figure(figsize=(6,4))
    sns.countplot(x='readmitted', data=df)
    plt.title('Readmission distribution')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    else:
        plt.show()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=False)
    args = parser.parse_args()
    df = pd.read_parquet(args.input)
    plot_readmission_distribution(df, args.output)
