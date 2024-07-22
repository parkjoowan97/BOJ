R,C = map(int,input().split())
mapp = []
for _ in range (0,R):
    a = input()
    mapp.append(a)

moving = [(0,1),(-1,0),(1,0),(0,-1)]
ans = 0
visited = [False for _ in range (0,26)]
visited[ord(mapp[0][0]) - 65] = True
cnt = 1
def bfs(n,m):
    global ans
    global visited
    global cnt
    ans = max(ans, cnt)
    for k in range (0,4):
        nn,mm = n + moving[k][0], m + moving[k][1]
        if 0 <= nn < R and 0 <= mm < C and visited[ord(mapp[nn][mm]) - 65] == False:
            visited[ord(mapp[nn][mm])-65] = True
            cnt += 1
            bfs(nn,mm)
            visited[ord(mapp[nn][mm])-65] = False
            cnt -= 1
bfs(0,0)
print(ans)