'''
Short sample on using sentiwordnet to calculate the
sentiment for a given list of words
'''

# importing the library
from nltk.corpus import sentiwordnet as swn

# defining the list of words to be evaluated
#   (please note: they are all the same part-of-speech)
words = ['good', 'great', 'bad', 'terrible', 'happy', 'sad']

# looping into the list of words and printing the sentiment
for elem in words:
    print ('\nfor word', elem, 'sentiment is', swn.senti_synset(elem + '.a.01'))
    
