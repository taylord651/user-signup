from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
@app.route("/signup", methods=['POST'])
def signup():
    return render_template("signup.html")

@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form['username']    
    return render_template("welcome.html", username=username)

app.run()