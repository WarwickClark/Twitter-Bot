import tweepy
import time

api_key = '###'
api_secret_key = '###'
Access_token = '###'
Access_token_secret = '###'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(Access_token, Access_token_secret)
api = tweepy.API(auth)

FILE_NAME = "last_seen.txt"

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return
def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    for tweet in reversed(tweets):
        if '#ultimatebot' in tweet.full_text.lower():
            print(str(tweet.id) + ' _ ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Auto reply, like, and retweet work:)", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(15)