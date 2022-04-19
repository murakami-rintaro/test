import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
path = "dataset/data.txt"

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

print(docs)
print(terms)