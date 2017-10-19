
import os
from user import User
from recipes import RecipeCat
from flask import Flask, render_template, request, session, redirect, url_for

from app import app


"""Instantiating objects"""
newUser = User()
newRecipeCat = RecipeCat()

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
            return render_template('login.html', data=message)

        elif result == "blank fields":
            message = ("please fill all the fields")
            return render_template('register.html', data=message)

        elif result == "special characters in username":
            message = ("Special characters not allowed in field name")
            return render_template('register.html', data=message)
        elif result == "password less than 6":
            message = (
                "Password should have minimum six characters")
            return render_template('register.html', data=message)
        elif result == "username exists":
            message = ("Username has alredy been taken")
            return render_template('register.html', data=message)
        elif result == "password mismatch":
            message = ("password do not match")
            return render_template('register.html', data=message)
        elif result == "invalid email":
            error = "email must be a valid email"
            return render_template('register.html', data=error)
        elif result == "email registered":
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

@app.route('/create/', methods=['GET', 'POST'])
def createrecipecats():
    """Handles creation of recipe categories"""
    if  'email' in session:
        if request.method == "POST":
            sentence = request.form['category']
            Catlist = sentence.split(' ')
            category = ''.join(Catlist)
            owner = session['email']
            result = newRecipeCat.create(category, owner)
            print(category)
            if result == 2:
                error = "that name already exists"
                return render_template('create.html', data=error)
            if result == 3:
                error = "Provide a category name"
                return render_template('create.html', data=error)                   
            if result == 1:
                result = newRecipeCat.get_recipecat_lists()   
                return render_template('display.html', datas=result,)        
            return redirect('/display')
        else:
            return render_template('create.html')
    else:
        return render_template('login.html')

@app.route('/delete/<category>')
def delete(category):
    """define route to delete a recipe category"""
    if  'email' in session:
        res = newRecipeCat.get_recipecat_lists()
        if res:
            result = newRecipeCat.delete(category)
            if result == True:
                message = "successfully deleted"
                return redirect(url_for('display', data=message))
            else:
                message = "Category not deleted"
                return redirect(url_for('display', data=message))                
        else:
            message = "not found"
            return render_template('create.html', data=message)
    else:
        return render_template('create.html')
    return render_template('login.html')

@app.route('/display')
def display():
    if  'email' in session:
        if request.method == 'GET':
            result = newRecipeCat.get_recipecat_lists()
            return render_template('display.html', data = result)

    error = 'Log in to see your dashboard'           
    return render_template('login.html', data=error)    


@app.route('/addrecipe')
def addrecipe():
    return render_template("addrecipe.html")

@app.route('/logout')
def logout():
    """Handles requests to logout a user"""
    session.pop('email', None)
    return redirect(url_for('home'))    


