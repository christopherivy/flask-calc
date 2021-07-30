# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


# # @app.route('/math/<operation>')
# @app.route('/add')
# def add():
#     print(request.args)
#     a = request.args['a']
#     b = request.args['b']
#     result = int(a) + int(b)
#     return f'<h1>The answer I got is: {result}</h1>'


# @app.route('/sub')
# def sub():
#     print(request.args)
#     a = request.args['a']
#     b = request.args['b']
#     result = int(a) - int(b)
#     return f'<h1>The answer I got is: {result}</h1>'


# @app.route('/mult')
# def mult():
#     print(request.args)
#     a = request.args['a']
#     b = request.args['b']
#     result = int(a) * int(b)
#     return f'<h1>The answer I got is: {result}</h1>'


# @app.route('/div')
# def div():
#     print(request.args)
#     a = request.args['a']
#     b = request.args['b']
#     result = int(a) / int(b)
#     return f'<h1>The answer I got is: {result}</h1>'


# -----------------------------------
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route('/math/<operation>')
def all_math(operation):
    """ This is one function that will do all the math functions """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = operators[operation](a, b)
    print(a, b)

    return f"<h2>The answer is: {str(result)}<h2>"
