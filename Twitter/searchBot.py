import tweepy
import time

api_key = '###'
api_secret_key = '###'
Access_token = '###'
Access_token_secret = '###'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(Access_token, Access_token_secret)
api = tweepy.API(auth)

hashtag = "noexams"
tweetnumber =10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
searchBot()