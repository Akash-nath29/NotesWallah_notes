from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Text, nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    musics = db.relationship('Music', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    role = db.Column(db.String(10), default='user')
    profile_picture = db.Column(db.String(255), default='static/img/default.png')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(100), nullable=False)
    file_description = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(255), nullable=False)
    college = db.Column(db.String(255), nullable=True)
    posted_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_link = db.Column(db.String(100), nullable=False)
    music_name = db.Column(db.String(100), nullable=False)
    posted_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    commented_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
