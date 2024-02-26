from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import os
from werkzeug.utils import secure_filename
import random
# import datetime


app = Flask(__name__)

# 投稿できる数は10個で固定とする
post_num = 0
post_contents = [{'image_name': "", 'comment': 'N/A', 'username': 'N/A'} for _ in range(10)]


# app.config.from_pyfile('settings.py')
#
# db = SQLAlchemy()
# db.init_app(app)
# Migrate(app, db)


@app.route('/')
def home():
    return render_template('home.html')


# def random_order_index(num, registered):
#     ls = random.sample(range(num), num)
#     ls2 = []
#     for n in ls:
#         if n < registered:
#             ls2.append()


@app.route('/personal')
def personal():
    random_numbers = random.sample(range(10), 10)
    return render_template('yume_timeline.html', post_contents=post_contents, post_num=post_num, rnumbers=random_numbers)


# @app.route('/', methods=["POST"])
# def post():
#     global post_num, post_contents
#     post_contents[post_num]['comment'] = request.form.get('comment')
#
#     # 投稿ボタンが押された時の処理(画像生成)
#     # img = 画像生成処理
#     # post_contents[post_num]['image'] = img
#     # print(post_contents[post_num]['comment'])
#     post_num += 1
#     return redirect('/')


@app.route('/personal/upload', methods=["POST"])
def upload():
    global post_num, post_contents

    # 投稿した画像に対する処理
    file = request.files.get('file')
    file_name = secure_filename(file.filename)
    file_path = os.path.join('static/', file_name)
    file.save(file_path)
    post_contents[post_num]['image_name'] = file_name
    # print(post_contents[post_num]['image_name'])

    # 投稿した文章に対する処理
    post_contents[post_num]['comment'] = request.form.get('comment')

    # 投稿ボタンが押された時の処理(画像生成)
    # img = 画像生成処理
    # post_contents[post_num]['image'] = img
    # print(post_contents[post_num]['comment'])

    post_num += 1
    return redirect('/personal')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         input_username = request.form.get('input_username')
#         input_email = request.form.get('input_email')
#         if input_username == "admin" and input_email == "abcd1234":
#             return redirect(url_for("https://www.google.co.jp/"))
#         else:
#             return render_template('login.html', message="Login failure. Please try again.")
#     return render_template('home.html')


# @app.route('/<username>')
# def personal(username):
#     return render_template('yume_timeline.html', username=username)


# @app.route('/', methods=['GET'])
# def get():
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
