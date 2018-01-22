# Answer to a question on Flask mailing list
# http://librelist.com/browser//flask/2012/6/30/using-ajax-with-flask/
# NOTE: *REALLY* don't do the thing with putting the HTML in a global
#       variable like I have, I just wanted to keep everything in one
#       file for the sake of completeness of answer.
#       It's generally a very bad way to do things :)
#
from flask import (Flask, jsonify, render_template)
from twitter_streamer import StdOutListener
from tweepy import Stream, OAuthHandler
#from config import consumer_key, consumer_secret, access_token, access_token_secret

app = Flask(__name__)

#Twitter Credentials
'''consumer_key = "YfsfRUtv0Jstlvm0TLg8DrZNA"
consumer_secret = "Dx95SabGPVACrlQanwkajOnsfss0tWsyej8xO8rUKnf6N70Tyh"
access_token = "704330902432669696-pmTtYoAM3ywia3zAY5sWAEVkzhWUwan"
access_token_secret = "BSW1LmSmDZmNrDPL3KytWXgZeOTHo99Ee1vDu1FBc5EAJ"'''

consumer_key = ["YfsfRUtv0Jstlvm0TLg8DrZNA","M7Gxr21fzCQPOeQ8Rcm48Hskv","dWdHXN0Ko3CdQogLJ4Iy24Vl5"]
consumer_secret = ["Dx95SabGPVACrlQanwkajOnsfss0tWsyej8xO8rUKnf6N70Tyh","Q5U8VniK0p8nMHYjvxll6V1H6CvNc4XUKHxDdqM0JioGNkej3r","e9EPoegS4TuYYYIN5m2JM3rTv7FuhAL7mYkIRGJlZwS4sWm9G3"]
access_token= ["704330902432669696-pmTtYoAM3ywia3zAY5sWAEVkzhWUwan","2162065807-hm17ST1Tt26bUscsSICz3aXptrwswOyipGc6x61","952228942458511360-5U6duPS5q6duwywioruXCDIX0JJmfL6"]
access_token_secret=["BSW1LmSmDZmNrDPL3KytWXgZeOTHo99Ee1vDu1FBc5EAJ","93DS5hJ1NQnKeZhRar2pH59QEO3LKD3njP5A9SfobZfYm","xizYGYtT57LbgqqPxmRyy6o9VGwKdY0FckYBDm1LKNqCw"]


# OAuth process

auth = OAuthHandler(consumer_key[1], consumer_secret[1])
auth.set_access_token(access_token[1], access_token_secret[1])

l = StdOutListener()

@app.route('/')
def index():
    return render_template('newindex3.html')

@app.route('/ajax', methods=['POST'])
def ajax_request():
    stream = Stream(auth, l)
    stream.filter(track=['Bitcoin', 'BTC', 'bitcoins'], async=True)
    score = round(l.df.Sentiment.mean(), 4)
    numTweets = len(l.df)
    return jsonify(score=score, numTweets = numTweets)

if __name__ == "__main__":
    app.run(debug=True)


# 1. Integrate Spinner with Sentiment Score
# 2. Begin UI/UX Design

