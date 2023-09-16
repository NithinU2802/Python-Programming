import nltk
from nltk import word_tokenize, pos_tag

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

sentence = "The quick brown fox jumps over the lazy dog."

words = word_tokenize(sentence)

print(pos_tag(words))
