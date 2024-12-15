import sys
import heapq

N, M = map(int,input().split())
indegree = [0 for _ in range (N+1)]
path = [[] for _ in range (N+1)]

for _ in range (M):
    a,b = map(int,input().split())
    indegree[b] += 1
    path[a].append(b)
    
prior_solving = []
for i in range (1, N+1):
    if indegree[i] == 0:
        heapq.heappush(prior_solving,i)

answer = []
while prior_solving:
    x = heapq.heappop(prior_solving)
    answer.append(x)
    
    for y in path[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(prior_solving,y)
            
print(*answer)