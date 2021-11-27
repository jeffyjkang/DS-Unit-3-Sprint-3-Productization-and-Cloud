''' Main app/routing file for Twitoff '''
from flask import Flask, render_template
from .models import DB, User

# create app
def create_app():
    # Create and config an instance of the Flask app
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='home', users=users)

    return app
