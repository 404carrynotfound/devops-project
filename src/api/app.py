from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Flask app!'

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, welcome to the Flask app!'


@app.route('/goodbye', methods=['GET'])
def goodbye():
    return 'Goodbye! Thanks for visiting.'


if __name__ == '__main__':
    app.run(debug=True)
