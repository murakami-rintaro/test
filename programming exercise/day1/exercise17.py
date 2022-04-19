import io,sys
import numpy as np
import nlp
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
path = "dataset/data.txt"

def make_terms_and_docs(path : str):
    docs = []
    terms = set()

    with open(path) as f:
        s = [s.strip() for s in f.readlines()]
    for i in s:
        i = i.split("と")
        docs.append(i)
        for j in i:
            terms.add(j)
    terms = list(terms)

    return terms, docs

terms, docs = make_terms_and_docs(path)
tf_Idf = nlp.tf_idf(terms, docs)
l = len(tf_Idf)
cosine = np.zeros((l, l))
for i in range(l):
    for j in range(l):
        cosine[i][j] = nlp.cosine_sim(tf_Idf[i], tf_Idf[j])

print(cosine)