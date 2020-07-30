from flask import Flask, redirect
from flask import render_template
from flask import url_for
from flask import flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '2ad88b0774c7e2c6f6d4abb5689a3cbc'

posts = [
    {
        'author': 'Salvador Izquierdo-Bueno',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 29, 2020'
    },
    {
        'author': 'Ioana Nedelcu',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 30, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
