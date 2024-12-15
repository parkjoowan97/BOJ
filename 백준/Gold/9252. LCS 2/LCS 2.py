import sys
input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()

def f(s, t):
    m, n = len(s), len(t)
    dp_length = [[0] * (n+1) for _ in range (m+1)]
    dp_word = [["" for _ in range (n+1)] for _ in range (m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp_length[i][j] = dp_length[i-1][j-1] + 1
                dp_word[i][j] = dp_word[i-1][j-1] + s[i-1]
            else:
                if dp_length[i-1][j] > dp_length[i][j-1]:
                    dp_length[i][j] = dp_length[i-1][j]
                    dp_word[i][j] = dp_word[i-1][j]
                else:
                    dp_length[i][j] = dp_length[i][j-1]
                    dp_word[i][j] = dp_word[i][j-1]

    length = dp_length[-1][-1]
    lcs_str = dp_word[-1][-1]

    print(length)
    if length > 0:
        print(lcs_str)

f(s, t)