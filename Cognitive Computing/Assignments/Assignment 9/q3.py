import re
text = "Artificial Intelligence (AI) is used in industries like Healthcare, Finance, and Education. The impact is visible in over 100+ countries."

long_words = re.findall(r'\b\w{6,}\b', text)
numbers = re.findall(r'\b\d+\b', text)
capitalized = re.findall(r'\b[A-Z][a-z]*\b', text)
only_alpha = re.findall(r'\b[a-zA-Z]+\b', text)
vowel_words = [word for word in only_alpha if word[0].lower() in 'aeiou']

print("Words with more than 5 letters:", long_words)
print("Numbers in text:", numbers)
print("Capitalized words:", capitalized)
print("Only alphabetic words:", only_alpha)
print("Words starting with vowels:", vowel_words)
