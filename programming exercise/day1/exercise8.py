s = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace(",", "")
s = s.replace(".", "")
s = s.split()
d = {}
one = [1, 5, 6, 7, 8, 9, 15, 16, 19]
for i in range(len(s)):
    if i + 1 in one:
        d[s[i][0]] = i + 1
    else:
        d[s[i][:2]] = i + 1
print(d)