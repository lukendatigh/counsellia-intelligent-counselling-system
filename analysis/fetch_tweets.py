def fetch(twitter_handle):
	consumer_key = 'sTHuqr1R1bMveD8kg9pAX0PyY'
	consumer_secret = 'QnKOUUO1EVJ9VvBJx7Y2hAiSMhvRjuupW0z7TaLtH24j6Q2uQV'
	access_token = '2266614999-qHbyiV47jSPycclUivzqLfIK8fSJ0YVhrjW2ui2'
	access_token_secret = 'FJFo35DNr53A13L23W899hxUWYGPHov3go5FiWqOVgqqz'
	import tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	# fetch tweets
	no_of_tweets = 1000
	fetched_tweets = api.user_timeline(screen_name = twitter_handle, count = no_of_tweets, include_rts=False)
	
	return fetched_tweets
