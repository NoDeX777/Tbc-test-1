from ext import login_manager,db
from flask import render_template,request,redirect
from models import User
from flask_login import current_user,login_user,logout_user,login_required
def index():
    return render_template("index.html")
def register():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        picture_url = request.form["picture_url"]
        user = User(
            email = email, password = password ,username = username , picture_url = picture_url
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html",title = "register")
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email = email).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect('/')
    return render_template("login.html",title = "login")
@login_required
def admin():
    if request.method == "POST":
        id = request.form["userid"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        url = request.form["url"]
        if email != "":
            User.query.get(id).email = email
            db.session.commit()
        if password != "":
            User.query.get(id).password = password
            db.session.commit()
        if url != "":
            User.query.get(id).picture_url = url
            db.session.commit()
        if username != "":
            User.query.get(id).username = username
            db.session.commit()
    return render_template("admin.html",title = current_user.username,users = User.query.all())
def delete_user_page():
    return render_template("delete_user.html",users = User.query.all())
def delete_user(user_id):
    user = User.query.get(user_id)
    if current_user.admin.admin_level > user.admin.admin_level:
        db.session.delete(user)
        db.session.commit()
        return redirect("/delete/user")
    else:
        return render_template("delete_user.html",users = User.query.all(),message = "You Cant delete")
def logout():
    logout_user()
    return redirect('/')