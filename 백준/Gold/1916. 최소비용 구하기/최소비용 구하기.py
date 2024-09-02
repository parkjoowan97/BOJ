import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
gp = [[] for _ in range (0,N+1)]
for _ in range (0,M):
    a,b,cost = map(int,input().split())
    gp[a].append((b,cost))
start, end = map(int,input().split())
INF = int(1e9)
dist = [INF for _ in range (0,N+1)]
q = []
dist[start] = 0
heapq.heappush(q, (dist[start], start))
while q:
    distance, node = heapq.heappop(q)
    if dist[node] < distance:
        continue
    for next, next_dist in gp[node]:
        d = distance + next_dist
        if d < dist[next]:
            dist[next] = d
            heapq.heappush(q, (dist[next], next))
print(dist[end])
    