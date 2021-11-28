''' Retrieve tweets and users then create embeddings and poplate DB '''
import tweepy
import spacy
from dotenv import load_dotenv
import os
from pathlib import Path
from .models import DB, Tweet, User

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

AUTH = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
# TWITTER = tweepy.API(AUTH)
TWITTER = tweepy.Client(BEARER_TOKEN)

# user = 'nasa'
# twitter_user = twitter.get_user(user)
# tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='Extended')
# tweets[0].text
# tweets[1].retweet_count


# nlp model
nlp = spacy.load('my_model')
def vectorize_tweet(tweet_text):
    return nlp(tweet_text).vector

def add_or_update_user(username):
    try:
        # twitter_user = TWITTER.get_user(username)
        twitter_user = TWITTER.get_user(username=username)
        twitter_user_id = twitter_user.data.id
        print(User.query.get(twitter_user_id))
        # db_user = (User.query.get(twitter_user.id)) or User(id=twitter_user.id, name=username)
        db_user = (User.query.get(twitter_user_id)) or User(id=twitter_user_id, name=username)
        DB.session.add(db_user)
        # tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='Extended')
        tweets = TWITTER.get_users_tweets(id=twitter_user_id, exclude=['retweets', 'replies'])

        if tweets:
            db_user.newest_tweet_id = tweets.data[0].id

        for tweet in tweets.data:
            vectorized_tweet = vectorize_tweet(tweet.text)
            db_tweet = Tweet(id=tweet.id, text=tweet.text, vect=vectorized_tweet)
            db_user.tweets.append(db_tweet)
        DB.session.commit()
    except Exception as e:
        print('Error processing{}: {}'.format(username, e))
        raise e
