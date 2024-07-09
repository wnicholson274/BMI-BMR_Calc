def calculate_bmr(gender, weight_kg, height_cm, age_years):

    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) + (5.677 * age_years)
    elif gender.lower() == 'female':
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) + (4.330 * age_years)
    else:
        raise ValueError("Gender must be 'male' or 'female'")
    
    return bmr  