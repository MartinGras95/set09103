from flask import Flask, redirect, url_for, abort,request,session
app = Flask(__name__)

#session key
app.secret_key = 'secretkey'

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

#Displaying file
@app.route("/display/")
def display():
    return '<img src="'+url_for('static', filename='uploads/upload.png')+'"/>'

#Uploading file through site
@app.route("/upload/", methods=['POST','GET'])
def upload():
    if request.method =='POST':
        f = request.files['datafile']
        f.save('static/uploads/upload.png')
        return "File Uploaded"
    else:
        page='''
        <html>
        <body>
        <form action="" method="post" name="form" enctype="multipart/form-data">
            <input type="file" name="datafile" />
            <input type="submit" name="submit" id="submit"/>
        </form>
        </body>
        </html>
        '''
        return page,200

#URL VARIABLES
#@app.route('/hello/<name>')
#def hello(name):
#    return "Hello %s" % name

@app.route('/add/<int:first>/<int:second>')
def add(first,second):
    return str(first+second)

@app.route("/hello/")
def hello():
    name = request.args.get('name','')
    if name == '':
        return "no params supplied"
    else:
        return "Hello %s" %name

#Sessions
@app.route('/sessions/write/<name>/')
def write(name=None):
    session['name']=name
    return "Wrote %s into 'name' key of sessions" % name

@app.route('/sessions/read')
def read():
    try:
        if(session['name']):
            return str(session['name'])
    except KeyError:
        pass
    return "No session variable set for 'name' key"

#to remove key from session
@app.route('/session/remove/')
def remove():
    session.pop('name',None)
    return "Removed key 'name' from session"
