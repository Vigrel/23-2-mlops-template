import pickle

import pandas as pd


def train(df):
    pass


def save_train(file_name, model_file_name):
    df = pd.read_parquet(f"./data/{file_name}_processed.parquet")

    """ADD YOUR TRAIN FUNCTION"""
    model = train(df)

    with open(f"./models/{model_file_name}.pkl", "wb") as f:
        pickle.dump(model, f)
