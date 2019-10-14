from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'secretkey'
myuser = "martin123"
mypass = "password123"

@app.route('/')
def index():
   return "Hello World"


@app.route('/login/<username>/<password>/')
def login(username=None,password=None):
#    print(username + " " +password + " " +session['username'] +" " +session['password'] + " " +myuser)

    session['username'] = username
    session['password'] = password
    try:
        if(session['username']==myuser and session['password']==mypass):
            return "login OK"
        else:
            return "Login not OK"
    except:
        pass
     
