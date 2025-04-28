# app_web/dashboard.py

import dash
from dash import dcc, html
import plotly.express as px
import os
import sys

# Allow imports from src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data_handler import load_health_data
from health_metrics import calculate_bmi, determine_bmi_zone

# Load data
data_path = os.path.join('..', 'data', 'health_data.xlsx')
df = load_health_data(data_path)

# If BMI not already present, calculate it
if 'BMI' not in df.columns and 'Weight' in df.columns and 'Height' in df.columns:
    df['BMI'] = df.apply(lambda row: calculate_bmi(row['Weight'], row['Height']), axis=1)

# App initialization
app = dash.Dash(__name__)
app.title = "Personal Health Dashboard"

# Layout
app.layout = html.Div([
    html.H1('Personal Health Tracker', style={'textAlign': 'center'}),

    dcc.Graph(
        id='weight-trend',
        figure=px.line(df, x='Date', y='Weight', title='Weight Over Time')
    ),

    dcc.Graph(
        id='heart-rate-trend',
        figure=px.line(df, x='Date', y='HeartRate', title='Heart Rate Over Time')
    ),

    dcc.Graph(
        id='blood-pressure-trend',
        figure=px.line(df, x='Date', y=['SystolicBP', 'DiastolicBP'], title='Blood Pressure Over Time')
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
