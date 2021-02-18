from flask import Flask, escape

app = Flask(__name__)


@app.route('/index')
@app.route('/home')
@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)
