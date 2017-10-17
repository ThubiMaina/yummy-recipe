from flask import Flask, render_template, request, session, redirect, url_for,g
import os
from user import User
from app import app

app.secret_key = os.urandom(24)
"""Instantiating objects"""
newUser = User()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    """define method to register users"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        result = newUser.register(email, username, password, cpassword)

        if result == 1:
            session['user'] = username
            message = "Account created sucessfully"
            return render_template('login.html', data = message)
        elif result == 6:
            message = ("please fill all the fields")
            return render_template('register.html', data = message)
        elif result == 5:
            message = ("Special characters not allowed in field name")
            return render_template('register.html', data=message)
        elif result == 3:
            message = ("password do not match")
            return render_template('register.html', data=message)
        elif result == 2:
            error = "email must be a valid email"
            return render_template('register.html', data=error)
        elif result == 4:
            error = "email already registered"
            return render_template('register.html', data=error)
    return render_template('register.html')   

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = newUser.login(email, password)
        if result == 1:
            username = newUser.get_user_name(email)
            email = newUser.get_user_email(email)
            session['user'] = username
            session['email'] = email
            return render_template('home.html', data=session)
        elif result == 2:
            error = "Wrong Password"
            return render_template('login.html',data=error) 
        elif result == 3:
            error = "The user does not exist please register and try again"
            return render_template('login.html', data=error)    
        elif result == 4:
            error = "Please fill all the fields"
            return render_template('login.html', data=error)        
        else:
            error = "Wrong credentials please try again"
            return render_template ('login.html',data=error) 
    else:
        return render_template('login.html')

@app.route('/create/')
def create():
    return render_template("create.html")

@app.route('/display')
def display():
    return render_template('display.html')

@app.route('/addrecipe')
def addrecipe():
    return render_template("addrecipe.html")

@app.route('/logout')
def logout():
    """Handles requests to logout a user"""
    session.pop('email', None)
    return redirect(url_for('home'))    


