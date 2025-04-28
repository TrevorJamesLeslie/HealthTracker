# Dash app (initial MVP)
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import sys
import os

# Adjust import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from data_handler import load_health_data
from health_metrics import calculate_bmi, blood_pressure_zone

# Load your data
DATA_FILE = '../data/health_data.xlsx'  # update path if needed
df = load_health_data(DATA_FILE)

# Calculate BMI if missing
if 'BMI' not in df.columns and 'Weight' in df.columns and 'Height' in df.columns:
    df['BMI'] = df.apply(lambda row: calculate_bmi(row['Weight'], row['Height']), axis=1)

# Create app
app = dash.Dash(__name__)
app.title = "Personal Health Tracker"

# Layout
app.layout = html.Div([
    html.H1("Personal Health Dashboard"),
    
    dcc.Graph(
        id='weight-trend',
        figure=px.line(df, x='Date', y='Weight', title='Weight Trend Over Time')
    ),

    dcc.Graph(
        id='blood-pressure-trend',
        figure=px.scatter(df, x='Systolic', y='Diastolic', color=df['Date'].dt.year.astype(str),
                          title='Blood Pressure Scatter Plot')
    ),

    dcc.Graph(
        id='bmi-trend',
        figure=px.line(df, x='Date', y='BMI', title='BMI Trend Over Time')
    ),
])

# Run server
if __name__ == '__main__':
    app.run_server(debug=True)
