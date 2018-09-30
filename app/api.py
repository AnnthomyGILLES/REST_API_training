from flask import Flask, render_template, request, jsonify
from app.forms import CalculForm
import datetime

# Create instances of web application.
app = Flask(__name__)


@app.route('/timestamp', methods=['GET'])
def get_time():
    """Return the timestamp"""
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    return jsonify({'timestamp': time})


@app.route('/multiply', methods=['POST'])
def multiply(**kwargs):
    """Return product of two numbers."""
    if len(kwargs) == 2:
        x = kwargs.get('x', None)
        y = kwargs.get('y', None)
        result = x * y
        return result
    x = int(request.args['x'])
    y = int(request.args['y'])
    result = x * y
    return jsonify({'multiply': result})


@app.route('/subtract', methods=['POST'])
def subtract(**kwargs):
    """Return subtraction of two numbers."""
    if len(kwargs) == 2:
        x = kwargs.get('x', None)
        y = kwargs.get('y', None)
        result = x - y
        return result
    x = int(request.args['x'])
    y = int(request.args['y'])
    result = x - y
    return jsonify({'substract': result})


@app.route('/add', methods=['POST'])
def add(**kwargs):
    """Return sum of two numbers."""
    if len(kwargs) == 2:
        x = kwargs.get('x', None)
        y = kwargs.get('y', None)
        result = x + y
        return result
    x = int(request.args['x'])
    y = int(request.args['y'])
    result = x + y
    return jsonify({'addition': result})


@app.route('/divide', methods=['POST'])
def divide(**kwargs):
    """Return divide of two numbers."""
    if len(kwargs) == 2:
        x = kwargs.get('x', None)
        y = kwargs.get('y', None)
        try:
            result = x / y
            return result
        except ZeroDivisionError:
            return "Can't divide by zero."
        return result
    x = int(request.args['x'])
    y = int(request.args['y'])
    result = x / y
    return jsonify({'divide': result})


@app.route('/', methods=['GET', 'POST'])
def add_web():
    """This function adds two numbers."""

    form = CalculForm()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    if request.method == 'POST':
        choice = request.form['calculation']
        number1 = int(request.form['first_number'])
        number2 = int(request.form['second_number'])
        if choice == 'value_add':
            result = add(x=number1, y=number2)
        elif choice == 'value_substract':
            result = subtract(x=number1, y=number2)
        elif choice == 'value_mult':
            result = multiply(x=number1, y=number2)
        elif choice == 'value_divide':
            result = divide(x=number1, y=number2)
        return render_template('views.html', form=form, timestamp=timestamp, result=result)
    elif request.method == 'GET':
        result = ""
        return render_template('views.html', form=form, timestamp=timestamp, result=result)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500