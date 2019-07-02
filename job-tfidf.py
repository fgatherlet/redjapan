import os
from sklearn.feature_extraction.text import TfidfVectorizer
import lib.jpextract
import pickle

with open("/tmp/jobs") as input:
    vectorizer = TfidfVectorizer(analyzer=lib.jpextract.extract_noun, min_df=1, max_df=50)
    corpus = input.readlines()
    result = vectorizer.fit_transform(corpus)
    with open("tfidf-result", 'wb') as f:
        pickle.dump(result, f)
    with open("tfidf-vectorizer", 'wb') as f:
        pickle.dump(vectorizer, f)



