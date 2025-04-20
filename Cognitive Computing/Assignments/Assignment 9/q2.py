import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = "Artificial Intelligence helps in solving problems faster than humans. AI systems can learn from data and make predictions."
text = text.lower()
stop_words = set(stopwords.words("english"))
words = word_tokenize(text)
filtered_words = [w for w in words if w not in stop_words and w.isalpha()]

porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

porter_result = [porter.stem(w) for w in filtered_words]
lancaster_result = [lancaster.stem(w) for w in filtered_words]
lemmatized_result = [lemmatizer.lemmatize(w) for w in filtered_words]

print("Original Words:", filtered_words)
print("Porter Stemmer:", porter_result)
print("Lancaster Stemmer:", lancaster_result)
print("Lemmatization:", lemmatized_result)
