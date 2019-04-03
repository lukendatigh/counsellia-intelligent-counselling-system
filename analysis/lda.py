def lemmatize(text):
	'''
	function to perform lematization on text
	'''
	from nltk.stem import WordNetLemmatizer
	lemma = WordNetLemmatizer()
	list = text.split() # convert string to list
	results = [lemma.lemmatize(i) for i in list] # lemmatize list
	# results_string = ''.join(str(result) for result in results) #convert list to string
	return results


def preprocess(text):
	'''
	function to remove stopwords and lowercase what's left
	'''
	from gensim.utils import simple_preprocess
	from gensim.parsing.preprocessing import STOPWORDS as stopwords
	result = []
	for token in simple_preprocess(text):
		if token not in stopwords and len(token) > 3:
			result.append(lemmatize(token))
	return result


def collect_first_items(list_of_tuples):
    list_of_strings = []
    for tup in list_of_tuples:
        list_of_strings.append(tup[0])
    return list_of_strings


def lda(fetched_tweets):
	from gensim.corpora import Dictionary as make_dict
	from gensim.models import LdaModel as lda

	tweets = fetched_tweets
	tweets_string = ''.join(str(tweet.text) for tweet in tweets)

	import re
	pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
	cleaned_tweets = pattern.sub('', tweets_string)

	tokens = preprocess(cleaned_tweets)
	dictionary = make_dict(tokens)
	# count = 0
	# for k, v in dictionary.iteritems():
	#     print(k, v)
	#     count += 1
	#     if count > len(dictionary):
	#         break

	corpus = [dictionary.doc2bow(doc) for doc in tokens]

	lda_model =  lda(corpus, num_topics = 9, id2word = dictionary, passes=20)
	# print(lda_model)

	list_of_stringlists = []
	num_of_topics = 9
	for i in range(0, num_of_topics):
		list_of_tuples = lda_model.show_topic(i)
		list_of_strings = collect_first_items(list_of_tuples)
		list_of_stringlists.append(list_of_strings)

	return list_of_stringlists

	# print(lda_model.print_topics(num_topics=8))
