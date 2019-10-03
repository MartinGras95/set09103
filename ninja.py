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





#404 handler
@app.errorhandler(404)
def page_not_found(error):
    return "A ninja stole this page D:"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

