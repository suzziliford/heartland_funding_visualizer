from flask import render_template, flash, redirect, url_for, request, Flask, Markup
from flask_login import current_user, login_user, logout_user, login_required
from flask_cors import CORS
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, SearchByForm, SearchByFormLine, SearchByFormBar
from app.models import User, Data

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
        'author': {'username': 'Youhou'},
        'body': 'I hope the snow melts today'
        },
        {
        'author':{'username': 'Hero'},
        'body': 'Wear your helmet!'
        }
    ]

    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# @app.route('/display', method=['GET'])
# @login_required
# def pie_chart():
#     data = [

#     ]

@app.route('/data')
# @cross_origin()
def data():
    form = SearchByForm()
    year = form.year.data
    print(year)
    health_data = Data.get_request_ha_health()
    international_data = Data.get_request_ha_international()
    human_needs_data = Data.get_request_ha_human_needs()
    care_services_data = Data.get_request_ha_care_services()
    housing_data = Data.get_request_ha_housing()
    # print(health_data)
    # print(international_data)
    # print(human_needs_data)
    # print(care_services_data)
    # print(housing_data)
    return render_template('data.html', title='data', form=form, year=year, health_data=health_data, 
                           international_data=international_data, 
                           human_needs_data=human_needs_data, 
                           care_services_data=care_services_data,
                            housing_data=housing_data )
    
labels = [
    'International', 'Health', 'Human Needs and Rights', 
    'Housing', 'Care Services'
]


colors = [
    "rgb(142, 235, 142)", "rgb(111, 156, 228)", "rgb(144, 208, 237)", "#FEDCBA",
    "red", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    form = SearchByForm()
    year = form.year.data
    # print(year)
    international_data = Data.get_request_ha_international()
    health_data = Data.get_request_ha_health()
    human_needs_data = Data.get_request_ha_human_needs()
    housing_data = Data.get_request_ha_housing()
    care_services_data = Data.get_request_ha_care_services()
    values = [
        international_data['filings_with_data'][0]['totrevenue'],
        health_data['filings_with_data'][0]['totrevenue'],
        human_needs_data['filings_with_data'][0]['totrevenue'],
        housing_data['filings_with_data'][0]['totrevenue'],
        care_services_data['filings_with_data'][0]['totrevenue']
    ]

  
    return render_template('pie.html', title='pie', form=form, year=year, 
                             set=zip(values, labels, colors) )


@app.route('/bar', methods=['GET', 'POST'])
def bar():
    form = SearchByFormBar()
    year = form.year.data
    # print(year)
    health_data = Data.get_request_ha_health()
    international_data = Data.get_request_ha_international()
    human_needs_data = Data.get_request_ha_human_needs()
    care_services_data = Data.get_request_ha_care_services()
    housing_data = Data.get_request_ha_housing()
    values = [
        health_data['filings_with_data'][0]['totrevenue'],
        international_data['filings_with_data'][0]['totrevenue'],
        human_needs_data['filings_with_data'][0]['totrevenue'],
        care_services_data['filings_with_data'][0]['totrevenue'],
        housing_data['filings_with_data'][0]['totrevenue']
    ]


    # print (values)
    return render_template('line.html', title='line', form=form, year=year, health_data=health_data, 
                           international_data=international_data, 
                           human_needs_data=human_needs_data, 
                           care_services_data=care_services_data,
                            housing_data=housing_data,
                             max=80000000, labels=labels, values=values )