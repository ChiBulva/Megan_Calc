"""
'/<num1>/add/<num2>'
'/<num1>/sub/<num2>'
'/<num1>/mul/<num2>'
'/<num1>/div/<num2>'

I need these routes in flask and a Jinja template that will render the result, the two numbers and maybe even an equation
"""

from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/<int:num1>/add/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return render_template('result.html', num1=num1, num2=num2, operator='+', result=result)

@app.route('/<int:num1>/sub/<int:num2>')
def sub(num1, num2):
    result = num1 - num2
    return render_template('result.html', num1=num1, num2=num2, operator='-', result=result)

@app.route('/<int:num1>/mul/<int:num2>')
def mul(num1, num2):
    result = num1 * num2
    return render_template('result.html', num1=num1, num2=num2, operator='*', result=result)

@app.route('/<int:num1>/div/<int:num2>')
def div(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed"
    result = num1 / num2
    return render_template('result.html', num1=num1, num2=num2, operator='/', result=result)

@app.route('/m/<string:opp><int:num1>')
def sm_opp(opp, num1 ):
    try:
        if opp == 'sqrt':  # New square root operation
            result = math.sqrt(num1)  # Assumes num1 is the number you want the square root of
            operator = '√'
    except:   
        return "Error occored probably: Division by zero is not allowed"

    return render_template('result.html', num1=num1, operator=operator, result=result)

@app.route('/m/<int:num1>/<string:opp>/<int:num2>')
def m_opp(num1, opp, num2):
    try:
        if opp == 'sub':
            result = num1 - num2
            operator='-'
        elif opp == 'add':
            result = num1 + num2
            operator='+'
        elif opp == 'mul':
            result = num1 * num2
            operator='*'
        elif opp == 'div':
            if num2 != 0:  # Check for division by zero
                result = num1 / num2
                operator = '/'
    except:   
        return "Error occored probably: Division by zero is not allowed"

    return render_template('result.html', num1=num1, num2=num2, operator=operator, result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5555')
