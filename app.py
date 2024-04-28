from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travelator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TravelGroup(db.Model):
    __tablename__ = 'travel_group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    members = db.Column(db.String(255))  # A simple way to store members as a comma-separated list

    # Relationship to Expense
    expenses = db.relationship('Expense', backref='travel_group', lazy=True)

class Expense(db.Model):
    __tablename__ = 'expense'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    payer = db.Column(db.String(80), nullable=False)
    travel_group_id = db.Column(db.Integer, db.ForeignKey('travel_group.id'))

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()