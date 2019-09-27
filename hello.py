from flask import Flask, redirect, url_for, abort,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello Napier</h1>'

@app.route('/students')
def student_list():    
    return 'Martin Gras,Johnny Bravo'

@app.route('/private')
def private():
    # Test for user not logged trying to access private page
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return 'Login page'

#Custom 404 error message
@app.errorhandler(404)
def page_not_found(error):
    return "A ninja stole this resource!", 404

#Force error
@app.route('/force404')
def force404():
    abort(404)

#static image
@app.route('/static-example/img')
def static_example_img():
    start = '<img src="'
    url = url_for('static', filename='vmask.jpg')
    end = '">'
    return start+url+end, 200

@app.route('/account',methods=['GET','POST'])
def account():
    if request.method =='POST':
        print request.form
        name = request.form['name']
        return "Hello %s" % name
    else:
        page = '''
        <html><body>
            <form action="" method="post" name="form">
                <label for="name">Name:</label>
                <input type="text" name="name" id="name"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
            </body><html>'''
        return page

#URL VARIABLES
@app.route('/hello/<name>')
def hello(name):
    return "Hello %s" % name

@app.route('/add/<int:first>/<int:second>')
def add(first,second):
    return str(first+second)

