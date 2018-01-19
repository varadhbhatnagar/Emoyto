import tweepy

CONSUMER_KEY = 'dWdHXN0Ko3CdQogLJ4Iy24Vl5'
CONSUMER_SECRET = 'e9EPoegS4TuYYYIN5m2JM3rTv7FuhAL7mYkIRGJlZwS4sWm9G3'
ACCESS_TOKEN = '952228942458511360-5U6duPS5q6duwywioruXCDIX0JJmfL6'
ACCESS_TOKEN_SECRET = 'xizYGYtT57LbgqqPxmRyy6o9VGwKdY0FckYBDm1LKNqCw'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def analyze_status(text):

	if 'RT' in text[0:3]:
		return True
	else:
		return False

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
	
	if not analyze_status(status.text) :

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

