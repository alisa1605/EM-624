# This script reads a text file, clean it in part and generates a word cloud
#   using the words in the text

# Importing the required libraries
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
file_p = open("./stopwords_en.txt",'r')
ls = []
with file_p:
    for line in file_p:
        ls.append(line.strip('\n'))
# Read the whole text
file_read = open("cons.txt")
text_raw = file_read.read()

# Replace end of line character with space
text_raw.replace('\n', ' ')

# Save a lower-case version of each word to a list
words_list = []
for word in text_raw.strip().split(): 
	words_list.append(word.lower())

# Eliminate non alpha elements
text_list = [word.lower() for word in words_list if word.isalpha()]

# Transforming the list into a string for displaying
text_str = ' '.join(text_list)

# Crating and updating the stopword list
stpwords = set(ls)


# Defining the wordcloud parameters
wc = WordCloud(background_color="white", max_words=2000,
               stopwords=stpwords)

# Generate word cloud
wc.generate(text_str)

# Store to file
wc.to_file('conswithoutmax.png')

# Show the cloud
plt.imshow(wc)
plt.axis('off')
plt.show()
