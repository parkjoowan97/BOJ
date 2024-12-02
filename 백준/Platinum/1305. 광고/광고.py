import sys

def compute_prefix_function(s):
    L = len(s)
    pi = [0] * L
    for i in range(1, L):
        k = pi[i - 1]
        while k > 0 and s[i] != s[k]:
            k = pi[k - 1]
        if s[i] == s[k]:
            k += 1
        pi[i] = k
    return pi

def minimal_ad_length(L, s):
    pi = compute_prefix_function(s)
    p = L - pi[-1]
    return p

def main():
    input = sys.stdin.readline
    L = int(input())
    s = input().rstrip()
    result = minimal_ad_length(L, s)
    print(result)

if __name__ == "__main__":
    main()