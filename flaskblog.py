from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

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

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')
