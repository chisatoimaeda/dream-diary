from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


app = Flask(__name__)


# app.config.from_pyfile('settings.py')
#
# db = SQLAlchemy()
# db.init_app(app)
# Migrate(app, db)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/<username>')
def personal(username):

    if request.form.get('input_username') == "admin" and request.form.get('input_email') == "abcd1234":
        return render_template('personal_home.html', username=username)


# @app.route('/', methods=['GET'])
# def get():
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
