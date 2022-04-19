import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
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

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
test_tf = tf(terms, docs)
for i in test_tf:
    tmp = []
    for j in i:
        res = "tf(" + j[0] + ", " + str(j[1]) + ") = " + str(j[2])
        tmp.append(res)
    print(" ".join(tmp))