from flask import Flask, render_template, redirect,request, session,flash,url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from alpha_vantage.timeseries import TimeSeries
import plotly.graph_objects as go
import os
from bsedata.bse import BSE
import requests

from pprint import pprint
# WSGI Application
# Defining upload folder path
# UPLOAD_FOLDER = os.path.join('static', 'uploads')
# # # Define allowed files
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
 
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name for template path
# The default folder name for static files should be "static" else need to mention custom folder for static path
app = Flask(__name__, template_folder='templates', static_folder='static')
# Configure upload folder for Flask application
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLAlCHEMY_ECHO']= True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(120),primary_key=True)
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(120))
    age = db.Column(db.Integer)
    coins=db.Column(db.Integer)

    def __repr__(self):
        return f"User('{self.email})'"


def plot_stock_graph(company_name, plot_file):
    # Set your API key
    api_key = 'EYFNIHUGCU4SZMGU'

    # Create an instance of the TimeSeries class
    ts = TimeSeries(key=api_key,output_format='pandas')

    # Get the intraday stock data for the specified symbol
    data, _ = ts.get_daily(symbol=company_name)

    # Create the plot using Plotly
    fig = go.Figure(data=go.Scatter(x=data.index, y=data['4. close']))
    fig.update_layout(title=f'Stock Data for {company_name}',
                      xaxis_title='Time',
                      yaxis_title='Closing Price')

    # Save the plot as HTML file with the unique file name
    
    plot_path = os.path.join('static', plot_file)
    print(plot_path)
    fig.write_image(plot_path,format='png')
    
    return plot_path
    
# b = BSE()
# tg = b.topGainers()
# pprint(tg)
# tl=b.topLosers()
# pprint(tl)
# @app.route('/login')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id',None)
        session["email"] = request.form.get("email")
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        # user =[x for x in users if x.email==email][0]
        if user and user.password == password:
            # return render_template('hometest.html')
            print('Login Success')
            print(user.name)
            return redirect(url_for('dashboard'))
        else:
            flash("Wrong login details!!")
        return redirect(url_for('login'))
    return render_template('login.html', title='Login')

b = BSE()
tg = b.topGainers()
# pprint(tg.securityID)
tl=b.topLosers()
# pprint(tl)
@app.route('/market')
def market():
    # tgain=[]
    # tloss=[]

    # for t in tg:
    #     t_gain=t['securityID']
    #     print(t_gain)
    #     tgain.append(t_gain)
    # for t in tl:
    #     t_loss=t['securityID']
    #     print(t_loss)
    #     tloss.append(t_loss)
    if not session.get("email"):
        return redirect("/login")
    # print(tg['securityID'])
    # return render_template('marketstats.html',tg=tgain,tl=tloss)
    return render_template('marketstats.html',title="Market Statistics", tg=tg,tl=tl)

@app.route('/dashboard')
def dashboard():
    if not session.get("email"):
        return redirect("/login")
    email=session.get('email')
    sess = db.session.query(User).filter_by(email=email)
    for ses in sess:
        print(ses.name)
    return render_template('dashboard.html',sess=sess,title='Dashboard')

api_key = 'EYFNIHUGCU4SZMGU'

@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get("email"):
        return redirect("/login")
    if request.method == 'POST' :
        company_n = request.form['companyn']
        qty=request.form['qty']
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=EYFNIHUGCU4SZMGU'
        print(url)
        r = requests.get(url)
        data = r.json()
        print(data)
        for i in data:
            print(i)
        s=153*int(qty)
        print(s)
        s=1000-s
        e=session.get('email')
        admin = User.query.filter_by(email='madhuriramakrishnan19@siesgst.ac.in').first()
        print(e)
        print(admin)
        admin.coins=s
        print(admin)
        db.session.commit()
        return render_template('index.html')
       
    # if request.method == 'POST':
    #     company_name = request.form['company']
    #     plot_file = f"{company_name.lower()}.png"  # Generate unique file name
    #     plot_stock_graph(company_name, plot_file)
    #     # print(p)
    #     return render_template('index.html',p=plot_file,title="Trade live")
    return render_template('index.html',title='Trade live')

# @app.route('/register')
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        password= request.form['password']
        age = request.form['age']
        coins=1000
        # hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name,email=email, password=password,age=age,coins=coins)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        flash('Your register successs!')
        print('Register Success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register')

if __name__=='__main__':
    app.run(debug=True)