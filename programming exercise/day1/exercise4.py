import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
s = "パタトクカシーー"
for i in range(2):
    print("".join([ s[j] for j in range(len(s)) if j % 2 == i]))