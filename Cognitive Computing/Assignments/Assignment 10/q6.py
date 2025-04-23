from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
import numpy as np

text = "data is the new oil. data helps in smart decisions. smart tools use data."

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
seq = tokenizer.texts_to_sequences([text])[0]

input_seq = []
for i in range(1, len(seq)):
    part = seq[:i+1]
    input_seq.append(part)

max_len = max(len(x) for x in input_seq)
input_seq = pad_sequences(input_seq, maxlen=max_len)

X = input_seq[:, :-1]
y = input_seq[:, -1]

total_words = len(tokenizer.word_index) + 1

model = Sequential()
model.add(Embedding(total_words, 10, input_length=max_len-1))
model.add(LSTM(100))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.fit(X, y, epochs=200, verbose=0)

seed = "data"
for i in range(3):
    seq_input = tokenizer.texts_to_sequences([seed])[0]
    seq_input = pad_sequences([seq_input], maxlen=max_len-1)
    pred = model.predict(seq_input, verbose=0)
    next_id = np.argmax(pred)
    for word, index in tokenizer.word_index.items():
        if index == next_id:
            seed += " " + word
            break

print("Generated Text:", seed)
