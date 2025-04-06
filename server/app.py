#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route: Displays the required h1 heading
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print route: Prints the parameter to console and displays it in the browser
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Display in browser

# Count route: Displays numbers from 0 to parameter-1 on separate lines
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return numbers

# Math route: Performs the specified operation on two numbers
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400  # Handle invalid operations
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)