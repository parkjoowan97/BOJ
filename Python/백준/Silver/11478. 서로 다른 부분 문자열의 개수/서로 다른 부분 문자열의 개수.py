s = input()
n = len(s)
words = set()
for i in range (1,n+1): #length
    for k in range (0,n-i+1): #startpoint
        words.add(s[k:k+i])
words = list(words)
print(len(words))