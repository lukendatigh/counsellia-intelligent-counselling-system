def fetch(twitter_handle):
	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_token_secret = ''
	import tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	# fetch tweets
	no_of_tweets = 1000
	fetched_tweets = api.user_timeline(screen_name = twitter_handle, count = no_of_tweets, include_rts=False)
	
	return fetched_tweets
