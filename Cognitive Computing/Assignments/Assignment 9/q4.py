import re

def custom_tokenize(txt):
    txt = re.sub(r'[^\w\s\'.-]', '', txt)
    tokens = txt.split()
    return tokens

def clean_text_regex(txt):
    txt = re.sub(r'\S+@\S+', '<EMAIL>', txt)
    txt = re.sub(r'https?://\S+|www\.\S+', '<URL>', txt)
    txt = re.sub(r'\+91\s?\d{10}|\d{3}-\d{3}-\d{4}', '<PHONE>', txt)
    return txt

sample_text = "Email us at team@example.com. Visit https://ai-world.org. Call +91 9876543210 or 123-456-7890. Our AI-based-tools are state-of-the-art."
custom_tokens = custom_tokenize(sample_text)
cleaned_text = clean_text_regex(sample_text)

print("Custom Tokens:", custom_tokens)
print("Cleaned Text:\n", cleaned_text)
