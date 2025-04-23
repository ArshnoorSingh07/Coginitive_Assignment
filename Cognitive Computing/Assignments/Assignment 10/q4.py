from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

text1 = "AI helps in making smart decisions using data."
text2 = "Blockchain keeps digital records safe and secure."

text1_clean = text1.translate(str.maketrans('', '', string.punctuation)).lower()
text2_clean = text2.translate(str.maketrans('', '', string.punctuation)).lower()

words1 = text1_clean.split()
words2 = text2_clean.split()

set1 = set(words1)
set2 = set(words2)

common = set1.intersection(set2)
union = set1.union(set2)
jaccard = len(common) / len(union)

print("Jaccard Similarity:", jaccard)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([text1, text2])
cos_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print("Cosine Similarity:", cos_sim[0][0])

if cos_sim[0][0] > jaccard:
    print("Cosine similarity shows better semantic overlap between texts.")
else:
    print("Jaccard similarity shows better common word overlap between texts.")
