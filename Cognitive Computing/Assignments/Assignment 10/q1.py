import nltk,re,string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.probability import FreqDist
nltk.download('punkt')
nltk.download('stopwords')
text="Technology is evolving rapidly, changing the way we interact with the world. Smartphones, AI, and cloud computing are some key innovations. These tools make life easier and more connected. We use technology for learning, working, and even entertainment. It is truly transforming every aspect of our lives."
text=text.lower()
text=text.translate(str.maketrans('', '', string.punctuation))
words_split=text.split()
words_token=word_tokenize(text)
stop_words=set(stopwords.words('english'))
filtered=[w for w in words_token if w not in stop_words]
fdist=FreqDist(filtered)
print('Words split: ',words_split)
print('\nWords Tokens: ',words_token)
print('\nFiltered: ',filtered)
fdist.plot(10)
