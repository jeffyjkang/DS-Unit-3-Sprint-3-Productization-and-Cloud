''' Main app/routing file for Twitoff '''
from flask import Flask, render_template
from .models import DB, User
from os import getenv
from pathlib import Path

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)
# create app
def create_app():
    # Create and config an instance of the Flask app
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        DB.drop_all()
        DB.create_all()

        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/update')
    def update():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Home')

    return app
