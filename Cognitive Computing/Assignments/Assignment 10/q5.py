from textblob import TextBlob
from wordcloud import WordCloud

review = "This tablet is fast and smooth. I love using it."

blob = TextBlob(review)
pol = blob.sentiment.polarity
sub = blob.sentiment.subjectivity

if pol > 0:
    result = "Positive"
elif pol < 0:
    result = "Negative"
else:
    result = "Neutral"

print("Polarity:", pol)
print("Subjectivity:", sub)
print("Sentiment:", result)

if result == "Positive":
    wc = WordCloud().generate(review)
    wc.to_file("positive_review.png")