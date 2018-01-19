
# coding: utf-8

# In[ ]:

import tweepy
from textblob import TextBlob
import re

CONSUMER_KEY = 'M7Gxr21fzCQPOeQ8Rcm48Hskv'
CONSUMER_SECRET = 'Q5U8VniK0p8nMHYjvxll6V1H6CvNc4XUKHxDdqM0JioGNkej3r'
ACCESS_TOKEN = '2162065807-hm17ST1Tt26bUscsSICz3aXptrwswOyipGc6x61'
ACCESS_TOKEN_SECRET = '93DS5hJ1NQnKeZhRar2pH59QEO3LKD3njP5A9SfobZfYm'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
a = []

def get_tweet_sentiment(tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
        
def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def analyze_status(text):

	if 'RT' in text[0:3]:
		return True
	else:
		return False

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
	
	if not analyze_status(status.text) and len(status.text) <= 120:
		
		a.append(status.text)
        b=status.text
        s=get_tweet_sentiment(clean_tweet(b))
        print (s)
        print (len(a))
        print len(b)
        if len(a)==10:
            exit()
            
        with open('fetched_tweets.txt','a') as tf:
            tf.write(status.text.encode('utf-8') + '\n\n')
    
        print(status.text + '\n')

    def on_error(self, status):
	print("Error Code : " + str(status))

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener , tweet_mode='extended')

 
myStream.filter(track=['#bitcoin' , '#BTC' , '#Bitcoin'],async=True,languages=['en'])
