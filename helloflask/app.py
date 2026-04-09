from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/square/<int:number>')
def square_number(number):
    return f'{number} squared is {number ** 2}.'

if __name__ == '__main__':
    app.run(debug=True)