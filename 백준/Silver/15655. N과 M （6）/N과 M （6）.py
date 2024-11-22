import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

answer = []
curr_list = []
def backtracking(n):
    if n == M:
        answer.append(" ".join(map(str,curr_list.copy())))
        return
    for i in range (n, N):
        if curr_list == [] or curr_list[-1] < num[i]:
            curr_list.append(num[i])
            backtracking(n+1)
            curr_list.pop()

backtracking(0)

for ans in answer:
    print(ans)
