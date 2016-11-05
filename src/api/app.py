from flask import Flask, render_template

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
    
if __name__== '__main__':
    app.run(debug = True, host = '0.0.0.0')
