"""The views"""
from user import User
from recipescat import RecipeCat
from flask import Flask, render_template, request, session, redirect, url_for,g 
from functools import wraps
from app import app

"""Instantiating objects"""
newUser = User()
newRecipeCat = RecipeCat()

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'email' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

@app.route('/')
def landingpage():
    return render_template('landingpage.html')

@app.route('/home')
@is_logged_in
def home():
    return render_template('home.html')    

@app.route('/register', methods=['GET', 'POST'])
def register():
    """define method to register users"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        result = newUser.register(email, username, password, cpassword)

        if result == True:
            session['user'] = username
            message = "Account created sucessfully"
            return render_template('login.html', data=message)

        elif result == 'You have blank fields':
            message = ("please fill all the fields")
            return render_template('register.html', data=message)

        elif result == "special characters in username":
            message = ("Special characters not allowed in field name")
            return render_template('register.html', data=message)
        elif result == "password less than 6":
            message = (
                "Password should have minimum six characters")
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
        if result == True:
            username = newUser.get_user_name(email)
            email = newUser.get_user_email(email)
            session['user'] = username
            session['email'] = email
            return render_template('home.html', data=session)
        elif result == "password mismatch":
            error = "Wrong Password"
            return render_template('login.html',data=error) 
        elif result == "not registered":
            error = "The user does not exist please register and try again"
            return render_template('login.html', data=error)    
        elif result == "blank fields":
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
    if g.user:
        if request.method == "POST":
            sentence = request.form['category']
            Catlist = sentence.split(' ')
            category = ''.join(Catlist)
            owner = session['email']
            newRecipeCat = RecipeCat(category, owner)
            result = newRecipeCat.create(category, owner)
            print(category)
            if result == "This category exists":
                error = "that name already exists"
                return render_template('create.html', data=error)
            if result == "blank category":
                error = "Provide a category name"
                return render_template('create.html', data=error)                   
            if result == True:
                result = newRecipeCat.get_recipecat_lists()   
                return render_template('display.html', datas=result,)        
            return redirect('/display')
        else:
            return render_template('create.html')
    else:
        return redirect('/login')

@app.route('/delete/<category>')
def delete(category):
    """define route to delete a recipe category"""
    if g.user:
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
    return redirect('/login')
@app.route('/display')
def display():
    if g.user:
        if request.method == 'GET':
            result = newRecipeCat.get_recipecat_lists()
            print(result)
            return render_template('display.html', datas = result)

    error = 'Log in to see your dashboard'           
    return render_template('login.html',data = error)

@app.route('/detail/<category>', methods=['GET', 'POST'])
def catdetail(category):
    """defining route to get the category lists"""
    if g.user:
        res = newRecipeCat.get_recipecat_list(category)
        recipes = newRecipeCat.getrecipes(category)
        if res:
            if request.method == 'GET':
                return render_template('detail.html', datas=res, posts=recipes)
            if request.method == "POST":
                sentence = request.form['recipe']
                post = request.form['description']
                recipelist = sentence.split(' ')
                recipe = ''.join(recipelist)
                owner = session['email']
                category = request.form['category']
                result = newRecipeCat.createrecipe(recipe, post, category)
            if result == True:
                return render_template('detail.html',datas=res, posts=recipes)
            elif result == "blank fields":
                error = "Please fill all the fields"
                return render_template('detail.html',datas=res, data=error)          
        else:
            return render_template('detail.html' )      
    else:
        return redirect('/login')


@app.route('/editcat/<category>', methods=['GET', 'POST'])
def editcategory(category):
    """defining route to get the category to edit"""
    if g.user:
        res = newRecipeCat.get_recipecat_list(category)
        if res:
            if request.method == 'GET':
                return render_template('edit.html', datas=res)

            if request.method == 'POST':
                old = request.form['old']
                new = request.form['category']
                owner = session['email']
                result = newRecipeCat.edit(old,new,owner)
        return redirect('/display')
    else:
        return redirect('/login')

@app.route('/deleterecipe/<category>/<recipe>',methods=['GET', 'POST'])
def deleterecipe(category,recipe):
    """Handles requests for deleting a recipe"""
    if g.user:
        recipes = newRecipeCat.getrecipes(category)
        res = newRecipeCat.get_recipecat_list(category)
        result = newRecipeCat.deleterecipe(recipe)
        if result == True:
            return render_template('detail.html',datas=res, posts=recipes)
        return render_template('detail.html',datas=res, posts=recipes)
    return redirect('/login')

@app.route('/editrecipe/<category>/<recipe>',methods=['GET', 'POST'])
def editrecipe(category, recipe):
    """Handles  requests for editing an item"""
    if g.user:
        recipes = newRecipeCat.getrecipes(category)
        res = newRecipeCat.get_recipecat_list(category)
        if request.method == 'GET':
            return render_template('editrecipe.html', posts=recipes, datas=res)

        if request.method == 'POST':
            recipe = request.form['oldrecipe']
            newrecipe = request.form['recipe']
            description = request.form['olddescription']
            newdescription = request.form['description']
            owner = session['email']
            result = newRecipeCat.editrecipe(recipe,newrecipe,
                description,newdescription,owner)
            if result ==True:
                return render_template('detail.html',datas=res, posts=recipes)
            return render_template('detail.html',datas=res, posts=recipes)
    else:
        return redirect('/login')


@app.route('/logout')
def logout():
    """Handles requests to logout a user"""
    session.pop('email', None)
    return redirect(url_for('landingpage'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']



