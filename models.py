from ext import db
from flask_login import UserMixin
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String,unique = True,nullable = False)
    email = db.Column(db.String,unique = True,nullable = False)
    picture_url = db.Column(db.String)
    password = db.Column(db.String,nullable = False)
    is_admin = db.Column(db.Boolean,default = False)
    admin = db.relationship("Admins",backref = "user_info")
class Admins(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    admin_level = db.Column(db.Integer,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    permisions = db.Column(db.String)