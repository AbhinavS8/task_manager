from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)

class Task(db.Model):
    id = db.Column(db.SmallInteger, primary_key=True)
    task_name = db.Column(db.VARCHAR(255), nullable=False)
    task_category = db.Column(db.VARCHAR(255), nullable=False)
    start_time = db.Column(db.TIMESTAMP, nullable=False)
    due_time = db.Column(db.TIMESTAMP, nullable=False)
    task_description = db.Column(db.Text, nullable=True) 
    completed = db.Column(db.Boolean, default=False)