from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<username>')
def user(username):
     return f'<h1>Profile for {username}</h1>'
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
