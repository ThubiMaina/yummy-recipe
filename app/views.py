from flask import Flask, render_template
from app import app



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register')
def register():
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


