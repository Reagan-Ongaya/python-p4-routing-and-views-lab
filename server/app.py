#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/')
def hello():
    return f'<param>hello</param>'

@app.route('/print/hello<parameter>')
def print_string(hello):
    print(hello)
    return f'<h3>Printed:hello</h3>'

@app.route('/print/<parameter>')
def print_param(parameter):
    print(parameter)
    return f'<param>{parameter}</param>'

@app.route('/count/<int:count_parameter>')
def count(count_parameter):
    numbers = '\n'.join(str(i) for i in range(1, count_parameter + 1))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
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

    if result is not None:
        return f'<h3>Result: {result}</h3>'
    else:
        return '<h3>Invalid operation or parameters</h3>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
