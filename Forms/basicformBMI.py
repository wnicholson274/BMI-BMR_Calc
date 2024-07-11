from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField

class BasicForm(FlaskForm):
    weight = StringField('Weight:')
    weight_unit = SelectField('Unit', choices=[('kg', 'Kilograms'), ('lbs', 'Pounds')])
    height = StringField('Height:')
    height_unit = SelectField('Unit', choices=[('cm', 'Centimeters'), ('in', 'Inches')])
    submit = SubmitField('Calculate BMR')
