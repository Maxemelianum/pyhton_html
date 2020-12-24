"""
"""

from flask import Flask, render_template

server = Flask(__name__)

messages = [
 {'username':'max_e','text':'Привет'},
 {'username':'fedyag','text':'Здравствуйте!'},
 {'username':'julia_a','text':'Добрый день'}
]

@server.route('/')
def hello():
    return '''Hello, World!
    <br>
    <a target="_blank" href=/index>Index</a>'''
@server.route('/get_messages')
def get_messages():
    return{'messages': messages
 }

@server.route('/index')
def index():
 name = 'Макс'
 return render_template("index.html")

@server.route('/day-<num>.html')
def day(num):
    return render_template(f"day-{num}.html")

server.run()