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

@app.route('/login')
def login():
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


