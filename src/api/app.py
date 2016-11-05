from flask import Flask, render_template
import random_bun

templates_path = "../templates"

app = Flask(__name__, template_folder = templates_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Kate')
def cakes():
    return render_template('kate.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/generate_bun')
def generate_bun():
    number = random_bun.random_number(10)
    return render_template('generate_bun.html' number=number)

if __name__== '__main__':
    app.run(debug = True, host = '0.0.0.0')
