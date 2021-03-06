from flask import (Flask, g, jsonify, render_template)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
