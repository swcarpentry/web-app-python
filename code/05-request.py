from flask import Flask, render_template
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

@app.route('/show/<name>')
def show_name(name):
    return render_template('show_name.html', name=name)

@app.route('/request/<remainder>')
def request(remainder):
    return render_template('request.html', remainder=remainder, title='with remainder')

@app.route('/request')
def request_default():
    return render_template('request.html', title='no remainder')

if __name__ == '__main__':
    app.run(debug=True)
