from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return "Hello World"

#Using Jinja to fill template
@app.route('/hello/<name>')
def hello(name=None):
    user = {'name':name}
    return render_template('hello.html',user=user)


#Conditional templating
@app.route('/condhello/')
@app.route('/condhello/<name>')
def condhello(name=None):
    return render_template('conditional.html', name=name)

#Looping through users
@app.route('/users/')
def users():
    names = ['Martin Gras','Sam Smith','Floyd Mayweather','Jerry Jenkins']
    return render_template('loops.html',names=names)

#Template Inheritance
#base page
@app.route('/father/')
def father():
    return render_template('base.html')

#Page that inherits the base page
@app.route('/father/son/')
def son():
    return render_template('base2.html')

#Another page that inherits the base page
@app.route('/father/grandson/')
def grandson():
    return render_template('base3.html')


#Simple randomizer website
@app.route('/randomizer/')
def randomizer():
    return render_template('randomizer.html')

#number randomizer extends randomizer
@app.route('/numrandomizer/')
def numrandomizer():
    randomnum = 10
    return render_template('numrandomizer.html',randomnum=randomnum)

#404 handler
@app.errorhandler(404)
def page_not_found(error):
    return "A ninja stole this page D:"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

