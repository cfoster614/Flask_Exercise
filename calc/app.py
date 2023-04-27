from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)




@app.route('/add')
def adding():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a, b)

    return str(result)

@app.route('/sub')
def subtracting():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def multiplying():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a, b)

    return str(result)

@app.route('/div')
def dividing():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a, b)

    return str(result)
       


        

