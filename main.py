from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

# @app.route("/")
# def index():
#     return render_template("user_signup.html", title="User Signup")

@app.route("/validate-signup")
def display_user_signup():
    return render_template("user_signup.html", title="User Signup")

def is_empty(entry):
  return entry == ""

def contains_space(entry):
    return " " in entry

def valid_entry(entry):
    is_valid = True
    if " " in entry or len(entry) < 3 or len(entry) > 20:
        is_valid = False
    return is_valid

def password_match(pw, check_pw):
    return pw == check_pw

def valid_email(email):
    is_valid = True
    if "@" not in email or "." not in email:
        is_valid = False
    return is_valid

@app.route("/validate-signup", methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if is_empty(username):
        username_error = "You must enter a username."
    elif not valid_entry(username):
        username_error = "Username must be between 3 and 20 characters and not contain a space."
        username = ""
    else:
        username = username
    
    if is_empty(password):
        password_error = "You must enter a password."
        password = ""
    
    elif not password_match(password, verify_password):
        password_error = "The entries for password and verify password must be identical."
        verify_password_error = "The entries for password and verify password must be identical."
        password = ""
        verify_password = ""
    else:
        password = password
        verify_password = verify_password
        if not valid_entry(password):
            password_error = "Password must be between 3 and 20 characters and not contain a space."
            password = ""

    if not is_empty(email) and (not valid_email(email) or not valid_entry(email)):
        email_error = "A valid email address must have a single '@', a single '.', contain no spaces, and be between 3 and 20 characters."
        email = ""

    if username_error == "" and password_error == "" and verify_password_error =="" and email_error == "":
        return redirect("/valid-signup")
    else:
        return render_template("user_signup.html", title="User Signup", username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, username=username, password="", verify_password="", email=email)

@app.route("/valid-signup", methods=['GET'])
def valid_signup():
    return "<h1>Success!</h1>"

app.run()