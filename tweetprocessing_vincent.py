import tweetstream
import string
import re

## ------------------------------------------------------------------------------------ ##
## Setting up the twitter stream.
## ------------------------------------------------------------------------------------ ##

stream = tweetstream.SampleStream("USERNAME", "PASSWORD")

# We need to get the basic positive and negative lists here, we use a preliminary list
# here.
basic_positive = [';\)', ':\)', ':p', ':-\)', 'winning', 'sweet', 'love', 'awesome']
basic_negative = [';\(', ':\(', ':d', ':-\(', 'shitty', 'losing', 'suck', 'sucks']

pos_str = '|'.join(basic_positive)
neg_str = '|'.join(basic_negative)

# Defining a function to score positive and negative words for tweets that contain the 
# the words.
def score(input, name):
	message = input.lower()
	if name in message:
		m_pos = re.findall(pos_str, message)
		m_neg = re.findall(neg_str, message)
		if len(m_pos) - len(m_neg) > 0:
			print [int(1), name]
		elif len(m_pos) - len(m_neg) < 0:
			print [int(0), name]
		else:
			pass
	
# Printing output of the form [score, name]. Score takes two values: 0 -negative sentiment
# and 1 - positive sentiment. Name spells either obama or romney.
for tweet in stream:
	if 'text' in tweet.keys() and len(tweet['text']) > 0 :
		score(tweet['text'], 'obama')
		score(tweet['text'], 'romney')
	else:
		pass
