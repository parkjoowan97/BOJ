import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())

answer = []
def back_tracking():
    if len(answer) == N:
        print(*answer)
        return
    for i in range (1, N+1):
        if i not in answer:
            answer.append(i)
            back_tracking()
            answer.pop()
back_tracking()