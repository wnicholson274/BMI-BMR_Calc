def calculate_bmr(weight, height, age, gender, weight_unit, height_unit):
    if weight_unit == 'lbs':
        weight = float(weight) * 0.45359237
    if height_unit == 'in':
        height = float(height) * 2.54

    if gender == 'male':
        bmr = 88.362 + (13.397 * float(weight)) + (4.799 * float(height)) - (5.677 * float(age))
    else:
        bmr = 447.593 + (9.247 * float(weight)) + (3.098 * float(height)) - (4.330 * float(age))
    return round(bmr, 2)