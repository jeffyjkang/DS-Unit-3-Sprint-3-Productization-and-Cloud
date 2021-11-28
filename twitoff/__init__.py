from .app import create_app

# APP = create_app()


# python commands:
# in app dir
#FLASKAPP=twitoff flask run

# in root dir
# FLASK_APP=twitoff flask shell

'''
Notes for setup:
in root, FLASK_APP=twitoff flask shell
import create_app
init create_app()
import DB
DB.create_all()
creates tables
'''

'''
Other commands
user1 = User.query.filter(User.name == 'nasa')
user1 = user1.one()
user1.tweets
'''