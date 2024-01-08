from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter

@app.route("/count/<int:parameter>")
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(1, parameter + 1))
    return numbers

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = ""
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "<h1>Error: Cannot Divide by zero</h1>"
    elif operation == "%":
        result = num1 % num2
    else:
        return "<h1>Error: Invalid operation</h1>"
    return f"<h1>Result: {result}</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
