from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/vaildate",methods=['POST'])
def vaildate():
    username = request.form['user']
    password = request.form['pass']
    vaild_pass = request.form['V_pass']
    email = request.form['e-mail']

    user_error = ''
    pass_error = ''
    v_pass_error = ''


    if len(username) < 3 or len(username) > 25:
        user_error = "That's not a vaild username"

    if " " in username:
        user_error = "That's not a vaild username"
        username =''

    if username == '':
        user_error = "That's not a vaild username"
        

    if len(password) < 3 or len(password) > 25:
        pass_error = "That's not a vaild password"
        password = ''

    if " " in password:
        pass_error = "That's not a vaild password"
        
    if vaild_pass != password:
        v_pass_error = "Password don't match"







    
    if not user_error and not pass_error and not v_pass_error:
        return render_template("vaildate.html", user = username)

    return render_template("index.html",user_error = user_error, 
    pass_error = pass_error,
     user = username,
     v_pass_error = v_pass_error)

@app.route("/")
def index():

     return render_template("index.html")

app.run()