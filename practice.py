from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def stor():
	return '<h1>Hello</h1>'


@app.route('/new/page', defaults = {'page' : 1})
@app.route('/new/page/<int:page>')
def index_page(page):
	return "Its number of tour page" + str(page)

def get_urls():
    return [
        url_for('index'),                # '/'
        url_for('list_posts'),           # '/posts/'
        url_for('list_posts', page=42),  # '/posts/page/42'
    ]

@app.route('/new/folder')
@app.route('/oldfolder', redirect_to = '/new/folder')
def interface():
	return "Redirection is done"



@app.route('/')
def index():
	return 'HI'


@app.route('/posts')
@app.route('/posts/<int:posts>')
def crreate(posts):
	return "Here we are --" + str(posts)

def get_urls():
	return [url_for('list_posts')]



@app.route('/99-bottles')
def viev_bottles():
	return render_template(
		'index.html',
		header = "HII",
		text = "бутылок стояло на столе, одна упала и разбилась",
		text_2 = 'Бутилок больше не осталось',
		users = ['Max', 'Ann', 'Bob'],
		hello = "Its a list"

		)

@app.route('/domen')
@app.route('/domen/<int:domen>')
def signin(domen):
	return str(domen) + "number of domen"


@app.route('/url/pattern')
def patterns(*args):
	return "This is your pattern" + str(123)
























