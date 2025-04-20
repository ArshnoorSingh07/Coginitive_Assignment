import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
nltk.download('punkt')
nltk.download('stopwords')

text = """Artificial Intelligence (AI) is transforming the world in incredible ways. From personalized recommendations on Netflix to autonomous cars and virtual assistants like Siri, the impact is huge. Technology in AI allows machines to learn, reason, and make decisions just like humans. With AI, industries like healthcare and finance are solving real problems faster than ever before. My curiosity in machine learning drives me to build smart models that can predict outcomes and understand language."""

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
words = word_tokenize(text)
sentences = sent_tokenize(text)
stop_words = set(stopwords.words("english"))
filtered_words = [w for w in words if w not in stop_words]
fdist = FreqDist(filtered_words)
print("Filtered Words:\n", filtered_words)
print("\nTop Words:")
fdist.plot(10)
