def n_gram(s, n : int):
    if type(s) == str:
        s = s.split()

    if len(s) < n:
        print("n is bigger than the size of s!")
        return

    se_n_gram = [s[i: i + n] for i in range(len(s) - n + 1)]
    print(se_n_gram)

    if n == 2:
        s = "".join(s)
        bi_gram = [s[i: i + 2] for i in range(len(s) - 1)]
        print(bi_gram)

s = input()
n = int(input())
n_gram(s, n)