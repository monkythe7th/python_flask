import os
from mods import auth, shopping
from flask import Flask, render_template, session 
from flask_session import Session

def create_app(test_config=None):
    app = Flask(__name__)
    # app.secret_key = "<DEV>"
    app.config.from_mapping(
        SECRET_KEY='dev',
        SESSION_TYPE='filesystem'
    )
    Session(app)
    # db.init_db(app)

    @app.route('/')
    def index():
        # db_test = db.get_db().list_collection_names()
        return render_template('index.html')

    app.register_blueprint(auth.bp)
    app.register_blueprint(shopping.bp)

    return app

if __name__ == '__main__':
    create_app().run(debug=True,host='0.0.0.0', port=5000)