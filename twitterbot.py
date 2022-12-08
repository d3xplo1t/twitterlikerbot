import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler(
    "", ""
)
auth.set_access_token(
    "",
    "",
)
# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Target Hashtags
KEY = '#python OR #django OR #javascript'    

while True:
    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=KEY).items():
            print('Tweet by @'+ tweet.user.screen_name)
            tweet.favorite()
            print('Liked') 
            time.sleep(200)
        
    except tweepy.errors.Forbidden:
        print("already liked :D")
        time.sleep(2)  
    except tweepy.errors.NotFound:
        print("tweet not found")
        time.sleep(2)
    except tweepy.errors.TooManyRequests:
        print("too many requests, lol")
        time.sleep(3600)

