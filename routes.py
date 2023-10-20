from flask_login import login_user, logout_user
from forms import Register, Login
from app import app, db
from flask import render_template, url_for, redirect, flash, session
from dbmodel import User


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/link')
def link():
    books = [
        {'id': 1, 'title': 'wahala pro max', 'isbn': 'jvojjgvof', 'year': '1960'},
        {'id': 2, 'title': 'problem dey oh', 'isbn': 'jvpfjvpijib', 'year': '1963'},
        {'id': 3, 'title': 'I saw it coming', 'isbn': 'kk okjzb[o', 'year': '1971'},
        {'id': 4, 'title': 'it being so long', 'isbn': 'kvkksfk', 'year': '1988'}
    ]
    return render_template("link.html", books=books)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user and attempted_user.check_password(form.password.data):
            login_user(attempted_user)
            flash(f'Login Successful', category='success')
            return redirect(url_for('link'))
        else:
            flash('Invalid User or Password', category='danger')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Error in {form[field].lable.text}: {error}', category=field)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('index'))


@app.route('/register', methods=["GET", "POST"])
def register():
    form = Register()
    if form.validate_on_submit():
        user_to_create = User(firstname=form.firstname.data,
                              lastname=form.lastname.data,
                              username=form.username.data,
                              email=form.email.data)
        user_to_create.set_password(form.password1.data)  # Hash and store the password
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        return redirect(url_for('link'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error creating this account: {err_msg}', category='danger')
    return render_template("register.html", form=form)


