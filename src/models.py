from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)



class ToDoTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    complete = db.Column(db.Boolean)
    alarm = db.Column(db.Boolean)

    def __repr__(self):
        return '<ToDoTask %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "task": self.task
        }