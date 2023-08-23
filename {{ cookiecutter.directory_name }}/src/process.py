import pandas as pd


def process(df):
    pass


def return_process(file_name):
    df = pd.read_csv(f"./data/{file_name}.csv")

    """ADD YOUR PROCESS FUNCTION"""
    df = process(df)

    df.to_parquet(f"./data/{file_name}_processed.parquet")
