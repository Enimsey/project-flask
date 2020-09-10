from flask import Flask, render_template, redirect, request,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #instance of class Flask

#app.config['SQLAlCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:26435120@localhost/quotes'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'postgres://efzntehcpkerbn:6b41c3a05fece8e8cc31dfb74b635963d854525b6c6379cfbc99920b2d7f26fe@ec2-54-247-118-139.eu-west-1.compute.amazonaws.com:5432/db1jnqn02hudma'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False # event notif system built in alchemy to track modifications to alchemy session, takes too much resources


db = SQLAlchemy(app) #instance of Alchemy

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index(): #view function will be called whenver the app is visited
	# ginger template passes arguments to template
	results = Favquotes.query.all()
	return render_template('index.html', results = results)

@app.route('/quotes')

def quotes(): 
	return render_template('quotes.html')

@app.route('/process', methods = ['POST']) #GET is the default

def process(): 
	author = request.form['author']
	quote = request.form['quote']
	quoteData = Favquotes(author = author, quote=quote)
	db.session.add(quoteData)
	db.session.commit()
	# redirect
	return redirect(url_for('index'))
