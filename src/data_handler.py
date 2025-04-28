# src/data_handler.py

import pandas as pd
import os

def load_health_data(file_path: str) -> pd.DataFrame:
    """
    Load the health data from an Excel file without cleaning or altering the data.
    
    Args:
        file_path (str): Relative or absolute path to the Excel file.
    
    Returns:
        pd.DataFrame: Loaded health data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")
    
    df = pd.read_excel(file_path)
    return df
