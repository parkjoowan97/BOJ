import sys
input = sys.stdin.readline

N = int(input())
mineFind = []
for _ in range (N):
    mineFind.append(list(input()))
    
movements = [(1,0), (-1,0), (0,1), (0,-1), (1,-1), (-1,-1), (1,1), (-1,1)]
answer = [[0 for _ in range (N)] for _ in range (N)]

for i in range (N):
    for j in range (N):
        if mineFind[i][j] != ".":
            answer[i][j] = "*"
        else:
            cnt = 0
            for movement in movements:
                ni, nj = i + movement[0], j + movement[1]
                if 0 <= ni < N and 0 <= nj < N and mineFind[ni][nj] != ".":
                    cnt += int(mineFind[ni][nj])
            
            if cnt >= 10:
                answer[i][j] = "M"
            else:
                answer[i][j] = cnt

for i in range (N):
    print("".join(map(str, answer[i])))