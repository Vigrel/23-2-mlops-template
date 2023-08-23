import pickle

import pandas as pd


def predict(file_name, model_file_name):
    model = pickle.load(open(f"./models/{model_file_name}.pkl", "rb"))
    df = pd.read_parquet(f"./data/{file_name}.parquet")
    df["y_pred"] = model.predict(df)
    df["y_pred"].to_csv(f"./data/{file_name}_predict.csv")
