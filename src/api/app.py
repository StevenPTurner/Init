from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_remplate(../'index.html')

@app.route('/cakes')
def cakes():
    return 'Cake!'

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
