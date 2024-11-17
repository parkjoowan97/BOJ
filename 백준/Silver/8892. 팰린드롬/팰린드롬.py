import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()
T = int(input())
for _ in range (T):
    K = int(input())
    words = []
    for _ in range (K):
        words.append(input())
        
    answers = []
    def answer(words):
        for word1, word2 in combinations(words, 2):
            word = word1 + word2
            reverse_word = word2 + word1
            n = len(word)
            check = False
            for i in range (0, n//2):
                if word[i] != word[n - 1 -i]:
                    check = True
                    break
                
            if check == False:
                return word
            
            check = False
            
            for i in range (0, n//2):
                if reverse_word[i] != reverse_word[n - 1 -i]:
                    check = True
                    break
            if check == False:
                return reverse_word
        return 0  
    print(answer(words))