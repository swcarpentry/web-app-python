from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello():
    return 'Hello page'

@app.route('/var/<name>')
def var_name(name):
    return 'Name provided is %s' % name

if __name__ == '__main__':
    app.run(debug=True)
