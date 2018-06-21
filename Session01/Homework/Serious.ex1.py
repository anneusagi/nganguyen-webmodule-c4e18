from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight, height):
    height_m = float(height/100)
    bmi = float(weight/(height_m**2))

    if bmi < 16:
        condition = "Severely underweight"
    elif bmi < 18.5:
        condition = "Underweight"
    elif bmi < 25:
        condition = "Normal"
    elif bmi <= 30:
        condition = "Overweight"
    else:
        condition = "Obese"


    # return "bmi = {0} => {1}".format(bmi,condition)  #Without render_template
    return render_template('bmi.html', bmi=bmi, condition=condition)  #With render_template
