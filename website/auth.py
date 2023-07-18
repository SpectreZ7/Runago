from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user,  login_required, logout_user, current_user



auth = Blueprint('auth', __name__)
@auth.route('/loginpage', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email') # Retrieve the value of the form field 'email'
        password = request.form.get('password') # Retrieve the value of the form field 'password'
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password): # checking if the provided password matches the hashed password stored in the user's record.
                flash('logged in successfully!', category='success')
                # Displaying a success message indicating successful login.
                login_user(user, remember=True)# Log in the user
                return redirect(url_for('pages.home'))# Redirect to the home page
            else:
                flash('Incorrect password, try again', category='error')
                 # Displaying an error message indicating incorrect password.
        else:
            flash('email does not exist', category='error')
            # Displaying an error message indicating that the provided email does not exist.
    return render_template("loginpage.html", user=current_user,)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signuppage', methods=['GET','POST'])
# The route '/signuppage' is accessible via both GET and POST methods.
def signuppage():
    if request.method == 'POST':
        # Checking if the current request method is POST.
        email = request.form.get('email') # Retrieve the value of the form field 'email'
        Username = request.form.get('Username')# Retrieve the value of the form field 'Username'
        password1 = request.form.get('password1') # Retrieve the value of the form field 'password1'
        password2 = request.form.get('password2') # Retrieve the value of the form field 'password2'

        user = User.query.filter_by(email = email).first()
        if user:
            flash('Email already exists', category='error')
            # Displaying an error message indicating that the email already exists.
        elif len(email) < 3:
            flash('email must be greater than 2 characters', category='error')
            # Displaying an error message indicating that the email must be at least 3 characters long.
        elif len(Username) < 4:
            flash('username must be greater than 3  characters', category='error')
            # Displaying an error message indicating that the username must be at least 4 characters long.
        elif password1 != password2:
            flash('password does not match', category='error')
            # Displaying an error message indicating that the password and confirm passwords do not match.
        elif len(password1) < 7:
            flash('password must be at least  7 characters', category='error')
            # Displaying an error message indicating that the password must be at least 7 characters long.
        else:
            #creates a new user object with the provided email, Username, and a hashed password generated using the generate_password_hash function.
            #password is hashed using the SHA-256 algorithm.
            new_user = User(email=email, Username=Username, password=generate_password_hash(password1, method='sha256')) 
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category='success')
            # Displaying a success message indicating successful account creation.
            return redirect(url_for('pages.home'))


    return render_template("signuppage.html", user=current_user)

    




    

