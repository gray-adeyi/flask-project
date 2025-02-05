from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db '
db = SQLAlchemy(app)

class Item(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(length=30),nullable=False,unique=True)
    price=db.Column(db.Integer(),nullable=False)
    barcode=db.Column(db.String(length=12),nullable=False, unique=True)
    description=db.Column(db.String(length=1024),nullable=False,unique=True)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')  
#this next line is for dynamic url
# @app.route('/about/<username>')
# def about_page(username ):
#     return f"<h1>This is the about page of {username}</h1>"

@app.route('/market')
def market_page():
    items =[
        {'id':1,'name':'Phone','barcode':'893212299897','price':500},
        {'id':2,'name':'Laptop','barcode':'1239854713165','price':900},
        {'id':3,'name':'Keyboard','barcode':'231985128446','price':150}
    ]
    return render_template('market.html', items=items)
if __name__ == '__main__':
    app.run(debug=True) 