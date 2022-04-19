import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import random
s = input().split()
ans = [s[0]]
for i in range(1, len(s) - 1):
    if len(s[i]) <= 3:
        ans.append(s[i])
    else:
        ans.append("".join(random.sample(list(s[i]), len(s[i]))))
ans.append(s[-1])
print(" ".join(ans))