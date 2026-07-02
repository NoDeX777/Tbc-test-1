from flask import Flask
from ext import login_manager, db
from models import User,Admins
from routes import *
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mybase.db"
app.config["SECRET_KEY"] = "1234"
db.init_app(app)
login_manager.init_app(app)
with app.app_context():
    db.create_all()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
app.add_url_rule("/","index",index)
app.add_url_rule("/delete/user","deluser",delete_user_page)
app.add_url_rule("/delete/user/<user_id>","delete",delete_user)
app.add_url_rule("/logout","logout",logout)
app.add_url_rule("/login","login",login,methods = ["get","post"])
app.add_url_rule("/register","register",register,methods = ["get","post"])
app.add_url_rule("/panel","panel",admin,methods = ["get","post"])
if __name__ == "__main__":
    app.run(debug=True)