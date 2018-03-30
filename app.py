
#
from flask import (Flask, jsonify, render_template, request)
from twitter_streamer import StdOutListener
from tweepy import Stream, OAuthHandler
from coinmarketcap import Market
cmp = Market()



#from config import consumer_key, consumer_secret, access_token, access_token_secret

app = Flask(__name__)

consumer_key = ["YfsfRUtv0Jstlvm0TLg8DrZNA","M7Gxr21fzCQPOeQ8Rcm48Hskv","dWdHXN0Ko3CdQogLJ4Iy24Vl5"]
consumer_secret = ["Dx95SabGPVACrlQanwkajOnsfss0tWsyej8xO8rUKnf6N70Tyh","Q5U8VniK0p8nMHYjvxll6V1H6CvNc4XUKHxDdqM0JioGNkej3r","e9EPoegS4TuYYYIN5m2JM3rTv7FuhAL7mYkIRGJlZwS4sWm9G3"]
access_token= ["704330902432669696-pmTtYoAM3ywia3zAY5sWAEVkzhWUwan","2162065807-hm17ST1Tt26bUscsSICz3aXptrwswOyipGc6x61","952228942458511360-5U6duPS5q6duwywioruXCDIX0JJmfL6"]
access_token_secret=["BSW1LmSmDZmNrDPL3KytWXgZeOTHo99Ee1vDu1FBc5EAJ","93DS5hJ1NQnKeZhRar2pH59QEO3LKD3njP5A9SfobZfYm","xizYGYtT57LbgqqPxmRyy6o9VGwKdY0FckYBDm1LKNqCw"]


# OAuth process

auth = OAuthHandler(consumer_key[0], consumer_secret[0])
auth.set_access_token(access_token[0], access_token_secret[0])

l = StdOutListener()

@app.route('/')
def index():
    return render_template('newindex3.html')

@app.route('/ajax', methods=['POST'])
def ajax_request():
	stream = Stream(auth, l)
	stream.filter(track=['BTC', 'Bitcoin', 'bitcoin'], async=True)
	score = round(l.df.Sentiment.mean(), 4)
	numTweets = len(l.df)
	lh=cmp.ticker("AUD",limit=1,convert='USD')
	return jsonify(score=score, numTweets = numTweets)


@app.route('/test', methods=['POST', 'GET'])
def test():
	if request.method == 'POST':
		id = request.form['id']
		print(id, type(id))
		return "Your id is : " + str(id) + " and type of id is : " + type(id)
	elif request.method == 'GET':
		return "GET REQUEST"

if __name__ == "__main__":
    app.run(debug=True)




# 1. Integrate Spinner with Sentiment Score
# 2. Begin UI/UX Design

