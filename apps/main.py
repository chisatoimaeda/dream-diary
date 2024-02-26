from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


app = Flask(__name__)

# 投稿できる数は固定とする
post_num = 0
descriptions = ["N/A" for _ in range(10)]


# app.config.from_pyfile('settings.py')
#
# db = SQLAlchemy()
# db.init_app(app)
# Migrate(app, db)


@app.route('/')
def home():
    return render_template('yume_timeline.html', descriptions=descriptions)


@app.route('/', methods=["POST"])
def post():
    global post_num, descriptions
    descriptions[post_num] = request.form.get('description')
    post_num += 1
    # 投稿ボタンが押された時の処理
    print(descriptions)
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
