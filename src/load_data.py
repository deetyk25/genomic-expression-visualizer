import pandas as pd

def load_expression_data(path):
    df = pd.read_csv(path, index_col=0)
    return df
