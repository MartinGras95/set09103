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

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
