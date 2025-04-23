import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

text = "Technology is evolving rapidly, changing the way we interact with the world. Smartphones, AI, and cloud computing are some key innovations. These tools make life easier and more connected. We use technology for learning, working, and even entertainment. It is truly transforming every aspect of our lives."

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()

stop_words = set(stopwords.words('english'))
clean_words = []
for word in words:
    if word.isalpha() and word not in stop_words:
        clean_words.append(word)

ps = PorterStemmer()
stemmed = []
for w in clean_words:
    stemmed.append(ps.stem(w))

lm = WordNetLemmatizer()
lemmatized = []
for w in clean_words:
    lemmatized.append(lm.lemmatize(w))

print("Stemmed Words:", stemmed)
print("Lemmatized Words:", lemmatized)
