import sys 
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
dict = {}
num = {}
for i in range (0,10):
    dict[i] = str(i)
    num[str(i)] = i
for i in range (0,26):
    dict[i + 10] = chr(i + 65)
    num[chr(i + 65)] = i + 10

summary = [0 for _ in range (0,36)]
#여기까지 기본 세팅
for _ in range (0,N):
    string =  input().rstrip()
    t = len(string)
    for i in range (0,t):
        summary[num[string[i]]] += (36 ** (t - i - 1))

K = int(input())

answer = 0

maximize = []
for i in range (0,36):
    maximize.append([dict[i], (35 - i) * summary[i]])

maximize.sort(key = lambda x: -x[1])


for i in range (0,K):
    answer += 35 * summary[num[maximize[i][0]]]

for i in range (K,36):
    answer += num[maximize[i][0]] * summary[num[maximize[i][0]]]


answer_string = []
while answer != 0:
    answer_string.append(dict[answer % 36])
    answer //= 36
    
answer_string = answer_string[::-1]
if answer_string != []:
    print("".join(s for s in  answer_string))
else:
    print("0")