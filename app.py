from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from Forms.basicform import BMRCalculator  # Import the form class from the basicform module
from bmrcalc import calculate_bmr

PORT = 5000
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = BMRCalculator()
    bmr_result = None

    if form.validate_on_submit():
        weight = form.weight.data
        weight_unit = form.weight_unit.data
        height = form.height.data
        height_unit = form.height_unit.data
        age = form.age.data
        gender = form.gender.data
        bmr_result = calculate_bmr(weight, height, age, gender, weight_unit, height_unit)

    return render_template('index.html', form=form, bmr_result=bmr_result)

if __name__ == '__main__':
    app.run(debug=True, host=('0.0.0.0'), port=PORT)