from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

# Define the base class
db = SQLAlchemy()

# Define the Users table
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    fullname = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Enum('student', 'admin', name='role_types'), default='student')

    # Relationships
    notes = db.relationship("Note", back_populates="user")

# Define the Subjects table
class Subject(db.Model):
    __tablename__ = 'subjects'

    subject_id = db.Column(db.String(50), primary_key=True)
    subject_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    # Relationships
    notes = db.relationship("Note", back_populates="subject")
    questions = db.relationship("Question", back_populates="subject")

# Define the Notes table
class Note(db.Model):
    __tablename__ = 'notes'

    note_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.String(50), db.ForeignKey('subjects.subject_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    content = db.Column(db.Text)
    file_path = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    # Relationships
    subject = db.relationship("Subject", back_populates="notes")
    user = db.relationship("User", back_populates="notes")

# Define the Questions table
class Question(db.Model):
    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.String(50), db.ForeignKey('subjects.subject_id'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    file_path = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    # Relationships
    subject = db.relationship("Subject", back_populates="questions")