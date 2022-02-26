from flask import Flask, render_template
app = Flask(__name__, static_folder='static') 

@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    from os import environ
    port = int(environ.get('PORT', 5000))
    app.run(debug=False, port=port,host='0.0.0.0')