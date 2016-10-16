import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Domsia2016@localhost:3306/myportrait'
db = SQLAlchemy(app)

class Labels(db.Model):
	__tablename__ = 'labels'
	contents = db.Column(db.String(100), primary_key=True)
	labelId = db.Column(db.Integer)
	title = db.Column(db.String(40))
	createUserId = db.Column(db.String(100))
	createtimestamp = db.Column(db.)
		
class AbilityLevel(db.Model):
	__tablename__ = 'abilityLevel'
	id = db.Column(db.Integer, primary_key=True)
	userId = db.Column(db.String(100), unique=True)
	username = db.Column(db.String(100), unique=False)
	labelId = db.Column(db.String(100))
	labelLevel = db.Column(db.Integer)

	def __init__(self, userId, username, labelId, labelLevel):
		self.userId = userId
		self.username = username
		self.labelId = labelId
		self.labelLevel = labelLevela

	def __repr__(self):
		return '<AbilityLevel %r>' %self.username


@app.route('/')
def hello():
	labels = Labels.query.all()
	labelStr = ''
	for label in labels:

		labelStr =labelStr + label. + ","
	return labelStr

if __name__ == '__main__':
	app.run()