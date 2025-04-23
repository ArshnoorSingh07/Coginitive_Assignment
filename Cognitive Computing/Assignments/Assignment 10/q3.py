from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

t1 = "The phone camera is very good."
t2 = "Battery does not last long."
t3 = "Amazing sound and display quality."

texts = [t1, t2, t3]

cv = CountVectorizer()
bow = cv.fit_transform(texts)
print("BOW Words:", cv.get_feature_names_out())
print("BOW Matrix:\n", bow.toarray())

tfidf = TfidfVectorizer()
result = tfidf.fit_transform(texts)

names = tfidf.get_feature_names_out()
for i in range(len(texts)):
    row = result[i].toarray()[0]
    top = row.argsort()[-3:][::-1]
    keywords = []
    for j in top:
        keywords.append(names[j])
    print("Top TF-IDF Words:", keywords)
