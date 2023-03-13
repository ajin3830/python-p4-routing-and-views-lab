#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# flask_app.py has a resource available at "/"
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# flask_app.py has a resource available at "/print/<parameter>"
# displays text of route in browser and console
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'         

# flask_app.py has a resource available at "/count/<parameter>"
@app.route('/count/<int:num>')
def count(num):
    # add each num to the empty string on a new line
    # you're NOT adding nums mathmatically here!!, it's like 
    # adding items to an empty list
    collection = ''
    for i in range(num):   
        collection += f'{i}\n'
    # return outside for loop or your loop will run then stop
    return collection

# flask_app.py has a resource available at "/math/<parameters>"
@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        # print(num1 + num2) wont work bc we want to return it
        # return num1 - num2 wont work bc num values aren't accessible 
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        return f'{num1 / num2}'
    elif operation == '%':
        return f'{num1 % num2}'
    
    return 'Operation not recognized. Please use one of the following: + - * div %'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
