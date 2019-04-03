def clean_tweet(tweet): 
	''' 
	function to clean tweet text by removing links, special characters 
	using simple regex statements. 
	'''
	import re
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 


def get_tweet_sentiment(tweet): 
	''' 
	function to classify sentiment of passed tweet 
	using textblob's sentiment method 
	'''
	# create TextBlob object of passed tweet text 
	from textblob import TextBlob
	analysis = TextBlob(tweet)
	# set sentiment 
	if analysis.sentiment.polarity > 0: 
		return 'positive'
	elif analysis.sentiment.polarity == 0: 
		return 'neutral'
	else: 
		return 'negative'


def get_percentage(sentiments):
	# counting sentiment
	positive = []
	negative = []
	neutral = []
	for sentiment in sentiments:
		if sentiment == 'positive':
			positive.append(sentiment)
		elif sentiment == 'negative':
			negative.append(sentiment)
		else:
			neutral.append(sentiment)

	positive_percent = round((100*(len(positive)/len(sentiments))), 2)
	negative_percent = round((100*(len(negative)/len(sentiments))), 2)
	neutral_percent = round((100*(len(neutral)/len(sentiments))), 2)
	dict_percent = {'positive': positive_percent, 
	'negative': negative_percent, 
	'neutral': neutral_percent}
	return dict_percent


def sentiment(fetched_tweets):
	fetched_tweets = fetched_tweets
	tweet_text = [tweet.text for tweet in fetched_tweets]

	cleaned_tweets = []
	for tweet in tweet_text:
		cleaned_tweets.append(clean_tweet(tweet))

	# assigning sentiment to corresponding tweet
	sentiments = []
	tweets = []
	for tweet in cleaned_tweets:
		sentiments.append(get_tweet_sentiment(tweet))
		tweets.append(tweet)

	# printing tweets and their sentiments
	# tweets_length = len(tweets)
	# for i in range(tweets_length):
	# 	print(f'Tweet:\n{tweets[i]}. \nSentiment:\n{sentiments[i]}\n')

	percent = get_percentage(sentiments)
	return percent