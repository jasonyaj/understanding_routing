from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/dojo')
def dojo():
    return 'dojo'


@app.route('/say/<name>')
def hello(name):
    return f'Hello {name.capitalize()}!'


@app.route('/repeat/<int:num>/<string:name>')
def multiply(num, name):
    output = ''

    for i in range(0, num):
        output += f'<p>{name}</p>'
    return output

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.'

if __name__ == "__main__":
    app.run(debug=True)
