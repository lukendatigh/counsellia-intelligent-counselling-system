def clean_text(text):
		'''
		Utility function to clean tweet text by removing links, special characters
		using simple regex statements.
		'''
		import re
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())


def preprocess(list):
	'''
	Function to remove stopwords and set to lowercase.
	Takes and returns and list
	'''
	from gensim.parsing.preprocessing import STOPWORDS as stopwords
	result = []
	for token in list:
		if token not in stopwords and len(token) > 3:
			token = token.casefold()
			result.append(token)
	return result


def word_frequency(fetched_tweets):
		tweet_texts = [tweet.text for tweet in fetched_tweets]

		# cleaning sentences (removing unneeded characters)
		cleaned_tweets = []
		for tweet in tweet_texts:
			cleaned_tweets.append(clean_text(tweet))

		# converting list of sentences, to list of sentence tokens
		tokens = []
		for sentence in cleaned_tweets:
			splitted = sentence.split()
			for token in splitted:
				tokens.append(token)


		# removing stopwords and lowercasing words
		words = preprocess(tokens)

		# counting and storing in a dictionary
		rough_frequency = {}
		for word in words:
			if word in rough_frequency:
				rough_frequency[word] += 1
			else:
				rough_frequency[word] = 1

		# sorting the dictionary
		# from collections import OrderedDict
		# sorted_dict = OrderedDict(sorted(rough_frequency.items(), key=lambda x: x[1], reverse=True))
		# frequency = dict(sorted_dict.items())
		# print(frequency)

		import collections
		mode_frequency = collections.Counter(rough_frequency).most_common(30)
		mode_frequency = dict(mode_frequency) # converting list of tuples to dict

		return mode_frequency
