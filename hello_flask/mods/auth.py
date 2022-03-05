import functools
from flask import render_template, Blueprint, request, url_for, g, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from api import create, read as getter, update

col = 'auth'
bp = Blueprint(col, __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        error = None
        user = getter.get_one(col,{'username': username})
        print(user)
        if not user:
            print(error = "invalid username")
        elif not check_password_hash(user['password'],password):
            error = "invalid password"
            print(error)

        if error is None:
            session.clear()
            session['user_id'] = user['username']
            return redirect(url_for('index'))

    return render_template('/auth/login.html')

@bp.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['uname']
        password_a = request.form['password_a']
        password_b = request.form['password_b']
        email = request.form['email']
        error = None

        if not username: error = "invalid username"
        if not (password_a and password_b) or check_password_hash(generate_password_hash(password_a),password_b): error = "invalid password"
        print(error)
        if error == None:
            try:
                user = {
                    'username': username,
                    'email': email,
                    'password': generate_password_hash(password_b)
                }

                u = getter.get_one(col,{'username': username})
                if u:
                    print(user['username'], 'already exists')
                else:
                    res = create.create(user,col)
                # return res.inserted_id
            except:
                pass
            else:
                return redirect(url_for('auth.login'))

    return render_template('/auth/signup.html')

@bp.route('/reset_password')
def reset_password():
    if request.method == 'POST':
        email = request.form['email']



@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.before_app_request
def load_logged_user():
    uid = session.get('user_id')

    if uid is None:
        g.user = None
    else:
        g.user = getter.get_one(col,{'username':uid})

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view