import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
node_ind = [0 for _ in range (0, N+1)]
answer = [1 for _ in range (0, N+1)]
gp = [[] for _ in range (0, N+1)]
for _ in range (0,M):
    a, b = map(int,input().split())
    gp[a].append(b)
    node_ind[b] += 1

deq = deque()
for i in range (1, N+1):
    # 해당 학기에 바로 이수할 수 있다느 뜻이므로
    if node_ind[i] == 0:
        deq.append(i)

while deq:
    x = deq.popleft()
    for y in gp[x]:
        node_ind[y] -= 1
        if node_ind[y] == 0:
            answer[y] = answer[x] + 1
            deq.append(y)
print(*answer[1:])