from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/') #This is the root
def landing_page():
  return render_template('index.html')  

@app.route('/ninjas') 
def ninjas():
    return render_template('ninjas.html')

@app.route('/ninjas/blue')
def blue_page():
    return ("<img src='../static/ninjas/leonardo.jpg'>")

@app.route('/ninjas/red')
def red_page():
    return ("<img src='../static/ninjas/raphael.jpg'>")

@app.route('/ninjas/purple')
def purple_page():
    return ("<img src='../static/ninjas/donatello.jpg'>")

@app.route('/ninjas/orange')
def orange_page():
    return ("<img src='../static/ninjas/michelangelo.jpg'>")

@app.route('/ninjas/<int:errorpath1>')
def wrong_page_number(errorpath1):
    return("<img src='../static/ninjas/notapril.jpg'>")

@app.route('/ninjas/<string:errorpath2>')
def wrong_page_string(errorpath2):
    return("<img src='../static/ninjas/notapril.jpg'>")

app.run(debug=True)