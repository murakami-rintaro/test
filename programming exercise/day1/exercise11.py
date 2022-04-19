import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
path = "dataset/data.txt"

with open(path) as f:
    s = f.read()
    print(s)