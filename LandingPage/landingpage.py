from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojo')
def new_user():
    return render_template('dojo.html')

app.run(debug=True)
