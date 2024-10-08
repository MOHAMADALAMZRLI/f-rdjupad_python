import pandas as pd

def read_data(file_path):
    """
    Läser in data från en CSV-fil med angiven filväg.
    """
    df_1 = pd.read_csv(file_path, encoding='latin1')  
    return df_1
