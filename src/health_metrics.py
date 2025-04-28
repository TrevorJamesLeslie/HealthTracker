# src/health_metrics.py

import pandas as pd

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """
    Calculate BMI using weight and height.
    
    Args:
        weight_kg (float): Weight in kilograms.
        height_cm (float): Height in centimeters.
    
    Returns:
        float: Calculated BMI.
    """
    if height_cm == 0:
        return None
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def determine_bmi_zone(bmi: float) -> str:
    """
    Determine the BMI zone based on standard ranges.
    
    Args:
        bmi (float): BMI value.
    
    Returns:
        str: Zone ('Good', 'Warning', 'Red Flag')
    """
    if bmi is None:
        return 'Unknown'
    if 18.5 <= bmi <= 24.9:
        return 'Good'
    elif 25.0 <= bmi <= 29.9:
        return 'Warning'
    else:
        return 'Red Flag'
