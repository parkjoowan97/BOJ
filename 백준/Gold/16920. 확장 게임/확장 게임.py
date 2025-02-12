import sys
from collections import deque
input = sys.stdin.readline

N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))

board = []
deq = [deque() for _ in range(P + 1)]
cnt = [0] * (P + 1)

for i in range(N):
    a = list(input().strip())
    board.append(a)
    for j in range(M):
        if a[j] != '.' and a[j] != '#':
            player = int(a[j])
            deq[player].append((i, j))
            cnt[player] += 1

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while True:
    expansion_check = False
    for player in range(1, P + 1):
        moves = S[player]
        if not deq[player]:
            continue

        for _ in range(moves):
            if not deq[player]:
                break

            new_area = deque()
            for _ in range(len(deq[player])):
                x, y = deq[player].popleft()
                for d in range (4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == '.':
                        board[nx][ny] = str(player)
                        cnt[player] += 1
                        new_area.append((nx, ny))
                        expansion_check = True
                        
            deq[player] = new_area

    if not expansion_check:
        break

cnt = cnt[1:]
print(*cnt)
