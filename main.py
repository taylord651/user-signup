from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

app.run()