from app import db
from datetime import datetime
from app import login_manager

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    username = db.Column(db.String(80), nullable=False,  unique=True)
    blogs =db.relationship('Blog',backref='owner')
    email = db.Column(db.String(120), nullable=False,  unique=True)
    fname = db.Column(db.String(120), nullable=False)
    lname = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120),nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Blog(db.Model):
    blog_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content=db.Column(db.Text(), nullable=False)
    pub_date=db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return '<Blog %r>' % self.title



