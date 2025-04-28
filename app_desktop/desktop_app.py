# PyQT app (later phase)
import sys
import os
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly.express as px
import pandas as pd

# Adjust path to import shared code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from data_handler import load_health_data
from health_metrics import calculate_bmi

class HealthDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Health Tracker - Desktop")
        self.setGeometry(100, 100, 1200, 800)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Load data
        DATA_FILE = '../data/health_data.xlsx'
        self.df = load_health_data(DATA_FILE)

        # Calculate BMI if missing
        if 'BMI' not in self.df.columns and 'Weight' in self.df.columns and 'Height' in self.df.columns:
            self.df['BMI'] = self.df.apply(lambda row: calculate_bmi(row['Weight'], row['Height']), axis=1)

        # Create and add plots
        self.add_plot(self.create_weight_trend())
        self.add_plot(self.create_blood_pressure_trend())
        self.add_plot(self.create_bmi_trend())

    def add_plot(self, fig):
        """
        Render a Plotly figure inside a QWebEngineView
        """
        html = fig.to_html(include_plotlyjs='cdn')
        view = QWebEngineView()
        view.setHtml(html)
        self.layout().addWidget(view)

    def create_weight_trend(self):
        return px.line(self.df, x='Date', y='Weight', title='Weight Trend Over Time')

    def create_blood_pressure_trend(self):
        return px.scatter(self.df, x='Systolic', y='Diastolic', color=self.df['Date'].dt.year.astype(str),
                          title='Blood Pressure Scatter Plot')

    def create_bmi_trend(self):
        return px.line(self.df, x='Date', y='BMI', title='BMI Trend Over Time')

def main():
    app = QApplication(sys.argv)
    dashboard = HealthDashboard()
    dashboard.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
