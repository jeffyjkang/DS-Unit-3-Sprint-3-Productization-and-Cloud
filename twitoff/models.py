'''SQLAlchemy models and utility functions for Twitoff App'''
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    ''' Twitter User Table that will correspong to tweets - SQLAlchemy syntax '''
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger) # keeps track of recent tweet

    def __repr__(self):
        return '<User: {}>'.format(self.name)

class Tweet(DB.Model):
    ''' Tweet text data - associated with User Table '''
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    vect = DB.column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet: {}>'.format(self.text)
