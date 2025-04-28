# Logic for zones, BMI calculation, alerts
def calculate_bmi(weight_kg, height_cm):
    """
    Calculate BMI from weight and height.
    """
    height_m = height_cm / 100
    if height_m <= 0:
        return None
    return round(weight_kg / (height_m ** 2), 2)

def bmi_category(bmi):
    """
    Determine BMI category.
    """
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

def blood_pressure_zone(systolic, diastolic):
    """
    Return BP zone color: 'green', 'yellow', 'red'
    """
    if systolic < 120 and diastolic < 80:
        return 'green'
    elif 120 <= systolic < 140 or 80 <= diastolic < 90:
        return 'yellow'
    else:
        return 'red'

def heart_rate_zone(hr):
    """
    Return Heart Rate zone: 'green', 'yellow', 'red'
    """
    if 60 <= hr <= 100:
        return 'green'
    elif 50 <= hr < 60 or 100 < hr <= 110:
        return 'yellow'
    else:
        return 'red'
