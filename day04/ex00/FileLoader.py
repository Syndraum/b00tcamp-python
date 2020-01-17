import pandas as pd

class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        print(data)
        return data

    def display(self, df, n)
        df.head()
