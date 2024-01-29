from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! This is my web app.'

@app.route('/about')
def about():
    return 'This is the about page. Please contact us through mail'
    #return 'Hello, World! Cette ligne fera bug le workflow'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
