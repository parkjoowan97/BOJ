import sys
input = sys.stdin.readline
N,M = map(int,input().split())
know_list = set(list(map(int,input().split()))[1:])
parties = []
for _ in range (0,M):
    a = set(list(map(int,input().split()))[1:])
    parties.append(a)
for _ in range (0,M):
    for party in parties:
        if len(party & know_list) != 0:
            know_list = know_list.union(party)
ans = 0
for party in parties:
    if len(party & know_list) == 0:
        ans += 1
print(ans)