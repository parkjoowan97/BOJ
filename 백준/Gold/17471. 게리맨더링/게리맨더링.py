import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def bfs(start, group, graph):
    q = deque([start])
    visited = set([start])
    population = 0
    while q:
        node = q.popleft()
        population += populations[node]
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor in group:
                visited.add(neighbor)
                q.append(neighbor)
    return population, len(visited) == len(group)

N = int(input())
populations = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    for neighbor in data[1:]:
        graph[i].append(neighbor)

min_diff = float('inf')

for i in range(1, N // 2 + 1):
    for group1 in combinations(range(1, N + 1), i):
        group2 = [x for x in range(1, N + 1) if x not in group1]
        
        pop1, valid1 = bfs(group1[0], set(group1), graph)
        pop2, valid2 = bfs(group2[0], set(group2), graph)
        
        if valid1 and valid2:
            min_diff = min(min_diff, abs(pop1 - pop2))

print(min_diff if min_diff != float('inf') else -1)
