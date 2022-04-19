import numpy as np
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from typing import List

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

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
test_idf = idf(terms, docs)

for i in test_idf:
    res = "idf(" + i[0] + ") = " + str(i[1])
    print(res)