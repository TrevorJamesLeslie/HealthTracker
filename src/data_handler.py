# Load/save/analyze data (shared between web & desktop)
import pandas as pd
from datetime import datetime

def load_health_data(filepath):
    """
    Load health data from an Excel or CSV file.
    """
    if filepath.endswith('.xlsx') or filepath.endswith('.xls'):
        df = pd.read_excel(filepath)
    elif filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    else:
        raise ValueError("Unsupported file format. Please use .xlsx or .csv")
    
    # Basic cleaning: ensure Date is datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        raise ValueError("Data must contain a 'Date' column.")
    
    return df

def save_health_data(df, filepath):
    """
    Save updated health data back to file.
    """
    if filepath.endswith('.xlsx') or filepath.endswith('.xls'):
        df.to_excel(filepath, index=False)
    elif filepath.endswith('.csv'):
        df.to_csv(filepath, index=False)
    else:
        raise ValueError("Unsupported file format.")
