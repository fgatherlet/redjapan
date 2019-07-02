import pickle

with open("tfidf-vectorizer", 'rb') as f:
    vectorizer = pickle.load(f)
with open("tfidf-result", 'rb') as f:
    result = pickle.load(f)

# print(vectorizer.inverse_transform(result)[0])
# pdb.set_trace()

def is_bigger_than_min_tfidf(term, terms, tfidfs):
    if tfidfs[terms.index(term)] > 0.1:
        return True
    return False

terms = vectorizer.get_feature_names()
result_ar = result.toarray()
for tfidfs in result_ar[0:100]:
    print([term for term in terms if is_bigger_than_min_tfidf(term, terms, tfidfs)])



