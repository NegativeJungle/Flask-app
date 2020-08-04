from flask import Flask, render_template



## My first flask aplication ####


## ##Testing basic routing for simple url 
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def stor():
	return '<h1>Hello</h1>'



@app.route('/')
def index():
	return 'HI'

##### Testing ended

#-----------------------------

## ## Implementing basic pagination for a url
@app.route('/new/page', defaults = {'page' : 1})
@app.route('/new/page/<int:page>')
def index_page(page):
	return "Its number of tour page" + str(page)


@app.route('/posts')
@app.route('/posts/<int:posts>')
def crreate(posts):
	return "Here we are --" + str(posts)


@app.route('/domen')
@app.route('/domen/<int:domen>')
def signin(domen):
	return str(domen) + "number of domen"

#### Implementing ended

#-----------------------------

## ## Geting urls
def get_urls():
    return [
        url_for('index'),                # '/'
        url_for('list_posts'),           # '/posts/'
        url_for('list_posts', page=42),  # '/posts/page/42'
    ]
#### Geting ended

#-----------------------------



## ## Redirecting from old_url to new_url
@app.route('/new/folder')
@app.route('/oldfolder', redirect_to = '/new/folder')
def interface():
	return "Redirection is done"

#### Redirecting ended

#------------------------------


## ## Making function for a rendering html template(index.html)
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

#### Rendering ended





























