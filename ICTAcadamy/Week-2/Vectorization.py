import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I am Nithin.",
    "K Ramakrishnan Collge of Technology.",
    "Fourth Year Student.",
    "Consider me as Document Data",
]

a = TfidfVectorizer()

tfidf_matrix = a.fit_transform(documents)

feature_names = a.get_feature_names_out()

out = pd.DataFrame(data=tfidf_matrix.toarray(), columns=feature_names)

print(out)
