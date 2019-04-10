from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

def is_email(mail):
    num = mail.count("@")
    num2 = mail.count(".")
    if num == 1 and num2 == 1:
        return True
    else:
        return False

@app.route("/vaildate",methods=['POST'])
def vaildate():
    username = request.form['user']
    password = request.form['pass']
    vaild_pass = request.form['V_pass']
    email = request.form['e-mail']

    user_error = ''
    pass_error = ''
    v_pass_error = ''
    email_error = ''

#username error vaildate
    if len(username) < 3 or len(username) > 20:
        user_error = "That's not a vaild username"
        username = ''
    elif " " in username:
        user_error = "That's not a vaild username"
        username =''
    elif username == '':
        user_error = "That's not a vaild username" 

#password error vaildate
    if len(password) < 3 or len(password) > 20:
        pass_error = "That's not a vaild password"
    elif " " in password:
        pass_error = "That's not a vaild password"

#checking password for match
    if vaild_pass != password:
        v_pass_error = "Password don't match"

    if email != '':
        if not is_email(email):
            email_error = "That's not a vaild email"
            email = ''
        elif len(email) < 3 or len(email) > 20:
            email_error = "That's not a vaild email"
            email = ''
        elif " " in email:
            email_error = "That's not a vaild email"
            email = ''
 
    if not user_error and not pass_error and not v_pass_error and not email_error:
        return render_template("vaildate.html", user = username)

    return render_template("index.html",user_error = user_error, 
    pass_error = pass_error,
     user = username,
     email = email,
     v_pass_error = v_pass_error,
     email_error = email_error)

@app.route("/")
def index():

     return render_template("index.html")

app.run()