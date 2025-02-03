from flask import render_template , request, redirect, url_for, session
from flask_login import login_required, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.model import db,User
from datetime import datetime
from flask import current_app as app

#Done and Verified...
@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                print(current_user)
                return redirect(url_for('index'))
            else:
                return render_template("login.html", alert = "Invalid Password!")
        else:
            return render_template("login.html", alert = "Not a Verified User...")
          
    return render_template("login.html")

#verified
@app.route("/signup", methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conformpassword = request.form['conformpassword']
        hashed_password = generate_password_hash(password)
        fullname = request.form['fullname']
        
        if not username or not password or not fullname or not conformpassword:
            return render_template("signup.html" , alert = "All fields are required...")
        
        if len(password) <6:
            return render_template("signup.html" , alert = "Password must be at least 6 characters long...")
        
        if password != conformpassword:
            return render_template("signup.html" , alert = "Password and Conform Password are not same...")


        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template("signup.html" , alert = "User Already Exits...")

        else:
            new_user = User(username=username, password=hashed_password, fullname = fullname)
            db.session.add(new_user)
            db.session.commit()
            return render_template("signup.html", success="Registration successful! ")
        
    return render_template("signup.html")
        
@app.route('/logout' , methods = ['POST', 'GET'])
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('index'))