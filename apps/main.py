from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import os
from werkzeug.utils import secure_filename
import datetime


app = Flask(__name__)

# 投稿できる数は10個で固定とする
post_num = 0
post_contents = [{'image_path': "", 'description': 'N/A', 'username': 'N/A'} for _ in range(10)]


# app.config.from_pyfile('settings.py')
#
# db = SQLAlchemy()
# db.init_app(app)
# Migrate(app, db)


@app.route('/')
def home():
    return render_template('yume_timeline.html', post_contents=post_contents, post_num=post_num)


# @app.route('/', methods=["POST"])
# def post():
#     global post_num, post_contents
#     post_contents[post_num]['description'] = request.form.get('description')
#
#     # 投稿ボタンが押された時の処理(画像生成)
#     # img = 画像生成処理
#     # post_contents[post_num]['image'] = img
#     # print(post_contents[post_num]['description'])
#     post_num += 1
#     return redirect('/')


@app.route('/upload', methods=["POST"])
def upload():
    global post_num, post_contents

    # 投稿した画像に対する処理
    file = request.files.get('file')
    file_name = secure_filename(file.filename)
    file_path = os.path.join('static/', file_name)
    file.save(file_path)
    post_contents[post_num]['image_path'] = file_path
    print(post_contents[post_num]['image_path'])

    # 投稿した文章に対する処理
    post_contents[post_num]['description'] = request.form.get('description')
    # 投稿ボタンが押された時の処理(画像生成)
    # img = 画像生成処理
    # post_contents[post_num]['image'] = img
    # print(post_contents[post_num]['description'])

    post_num += 1
    return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        input_username = request.form.get('input_username')
        input_email = request.form.get('input_email')
        if input_username == "admin" and input_email == "abcd1234":
            return redirect(url_for("https://www.google.co.jp/"))
        else:
            return render_template('login.html', message="Login failure. Please try again.")
    return render_template('login.html')


# @app.route('/<username>')
# def personal(username):
#     return render_template('yume_timeline.html', username=username)

# @app.route('/', methods=['GET'])
# def get():
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
