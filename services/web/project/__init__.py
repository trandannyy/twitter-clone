import os

from flask import Flask, jsonify, send_from_directory, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import sqlalchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
db_link = "postgresql://hello_flask:hello_flask@localhost:5432/hello_flask_dev"


##############################################
# Tutorial Section
##############################################


# class User(db.Model):
#     __tablename__ = "users"
#
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(128), unique=True, nullable=False)
#     active = db.Column(db.Boolean(), default=True, nullable=False)
#
#     def __init__(self, email):
#         self.email = email

##############################################

@app.route("/")
def root():
    print_debug_info()
    messages = [{}]

    username = request.cookies.get('username')
    password = request.cookies.get('password')
    good_credentials = are_credentials_good(username, password)

    return render_template('root.html', logged_in=good_credentials, messages=messages)


def print_debug_info():
    # GET method
    print('request.args.get("username")=', request.args.get("username"))
    print('request.args.get("password")=', request.args.get("password"))

    # POST method
    print('request.form.get("username")=', request.form.get("username"))
    print('request.form.get("password")=', request.form.get("password"))

    # cookies
    print('request.cookies.get("username")=', request.cookies.get("username"))
    print('request.cookies.get("password")=', request.cookies.get("password"))


def are_credentials_good(username, password):
    # CORRECT ?
    sql = sqlalchemy.sql.text('''
    SELECT screen_name, password
    FROM users
    WHERE screen_name = :username
    AND password = :password
    ''')

    # engine = sqlalchemy.create_engine(db_link, connect_args={
    #     'application_name': '__init__.py root()',
    # })
    # connection = engine.connect()
    res = db.session.execute(sql, {
        'username': username,
        'password': password
    })

    return res.first() is not None

    # NEED TO CONNECT TO ENGINE
    # for row in res.fetchall():
    #     print('row[0]=,' row[0])
    #     print('row[1]=,' row[1])

    #     if row[0] == :username and row[1] == :password:
    #         logged_in = True
    #     else:
    #         logged_in = False

    # if username == 'haxor' and password == '1337':
    #     return True
    # else:
    #     return False


@app.route("/login", methods=['GET', 'POST'])
def login():
    print_debug_info()
    username = request.form.get('username')
    password = request.form.get('password')
    print('username=', username)
    print('password=', password)

    good_credentials = are_credentials_good(username, password)
    print('good_credentials=', good_credentials)

    # first visit means no form submission
    if username is None:
        return render_template('login.html', bad_credentials=False, created=False)

    # form submitted, use POST method
    else:
        if not good_credentials:
            return render_template('login.html', bad_credentials=True, created=False)
        else:
            # if we get here, then logged in!
            # create cookies with username and password

            template = render_template('login.html', bad_credentials=False, created=False, logged_in=True)

            # return template

            response = make_response(template)
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            return response


@app.route("/logout")
def logout():
    print_debug_info()
    resp = make_response(render_template('logout.html', logged_in=False))
    resp.set_cookie('username', expires=0)
    resp.set_cookie('password', expires=0)
    return resp
    # return render_template('logout.html')


def valid_username(username):
    # check uniqueness of username
    sql = sqlalchemy.sql.text('''
    SELECT screen_name
    FROM users
    WHERE screen_name = :username
    ''')
    res = db.session.execute(sql, {
        'username': username
        })

    unique = True
    for row in res.fetchall():
        if row[0] == username:
            unique = False 
            break
    return unique

def valid_password(password, retyped):
    return (password == retyped)

@app.route("/create_user", methods=['GET', 'POST'])
def create_user():
    print_debug_info()
    username = request.form.get('username')
    password = request.form.get('password')
    retyped = request.form.get('retype password')
    print('username=', username)
    print('password=', password)
    print('retyped=', retyped)

    # first visit
    if retyped is None:
        return render_template("create_user.html", identical_user=False, password_different=False)
    # form submitted
    else:
        if valid_username(username) and not valid_password(password, retyped):
            return render_template("create_user.html", identical_user=False, password_different=True)
        elif not valid_username(username) and valid_password(password, retyped):
            return render_template("create_user.html", identical_user=True, password_different=False)
        elif not valid_username(username) and not valid_password(password, retyped):
            return render_template("create_user.html", identical_user=True, password_different=True)
        else:
            template = render_template("create_user.html", identical_user=False, password_different=False)
            
            sql = sqlalchemy.sql.text('''
            INSERT INTO users (id_users, screen_name, password)
            VALUES (:id_users, :username, :password)
            ''')
            res = db.session.execute(sql, {
            'id_users': 1010101023,
            'username': username,
            'password': password
            })
            db.session.commit();

            return render_template("login.html", bad_credentials=False, created=True)
        # HOW DO I GET RANDOM id_users???

    # return render_template("create_user.html", identical_user=True, password_wrong=True)


@app.route("/create_message")
def create_message():
    return render_template("create_message.html")


@app.route("/search")
def search():
    return render_template("search.html")


# def hello_world():
#     return jsonify(hello="world")


# @app.route("/static/<path:filename>")
# def staticfiles(filename):
#     return send_from_directory(app.config["STATIC_FOLDER"], filename)
#
#
# @app.route("/media/<path:filename>")
# def mediafiles(filename):
#     return send_from_directory(app.config["MEDIA_FOLDER"], filename)
#
#
# @app.route("/upload", methods=["GET", "POST"])
# def upload_file():
#     if request.method == "POST":
#         file = request.files["file"]
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
#     return """
#     <!doctype html>
#     <title>upload new File</title>
#     <form action="" method=post enctype=multipart/form-data>
#       <p><input type=file name=file><input type=submit value=Upload>
#     </form>
#     """
