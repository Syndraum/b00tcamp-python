import pandas as pd


class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        print(
            "Loading dataset of dimensions",
            data.shape[0], "x", data.shape[1])
        return data

    def display(self, df, n):
        print(df.head(n))
