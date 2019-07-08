from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
@app.route("/signup")
def display_form():
    return render_template("signup.html")

@app.route("/", methods=['POST'])
@app.route("/signup", methods=['POST'])
def validate_signup():

    username = request.form['username']    
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""
    
    if username == "":
        username_error = "Error: username required"
    else:
        if len(username) < 3 or len(username) > 20:
            username_error = "Error: please type a username that is 3-20 characters long"
            username = ""

    if password == "":
        password_error = "Error: password required"
        password = ""
    else:
        if len(password) < 3 or len(password) > 20:
            password_error = "Error: please type a password that is 3-20 characters long"
            password = ""

    if verify_password == "":
        verify_password_error = "Error: please verify your password"
        verify_password = ""
    else:
        if password != verify_password:
            verify_password_error = "Error: Password and Verify Password do not match"
            verify_password = ""

    if email != "":
        if len(email) < 3 or len(email) > 20:
            email_error = 'Error: Email is not valid. It must be 3-20 characters long.'
        elif " " in email:
            email_error = 'Error: Email is not valid. It must have no spaces.'
        else:
            if email != "" and "@" not in email and "." not in email:
                email_error = 'Error: Email is not valid. It must contain an "@" symbol, a "."'

    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template("signup.html",
            username = username,
            email = email,
            username_error = username_error, 
            password_error = password_error, 
            verify_password_error = verify_password_error, 
            email_error = email_error)


@app.route("/welcome", methods=["POST", "GET"])
def welcome():
    username = request.args.get('username')   
    return '<h1>Welcome, {0}!</h1>'.format(username)

app.run()