import numpy as np
from typing import List

def tf(term : List[str], doc : List[List[str]]):
    res = []
    for s in doc:
        tmp = []
        for t in term:
            tf = s.count(t) / len(s)
            tmp.append((t, s, tf))
        res.append(tmp)
    return res

def idf(term : List[str], doc : List[List[str]]):
    res = []
    for t in term:
        count = 0
        for s in doc:
            if t in s:
                count += 1
        idf = np.log10(len(doc) / count) + 1
        res.append((t, idf))
    return res

def tf_idf(term : List[str], doc : List[List[str]]):
    res_tf = tf(term, doc)
    res_tf = np.array([ [res_tf[i][j][2] for j in range(len(res_tf[i]))] for i in range(len(res_tf))])
    res_idf = idf(term, doc)
    res_idf = np.array([ res_idf[i][1] for i in range(len(res_idf))])
    res_tf_idf = res_tf * res_idf.T
    return res_tf_idf

if __name__ == '__main__':
    docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
    terms = ["リンゴ", "レモン", "ミカン"]

    print(tf_idf(terms, docs))
