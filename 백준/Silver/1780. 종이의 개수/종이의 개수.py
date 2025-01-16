import sys

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = {-1: 0, 0: 0, 1: 0}

def divide(row, col, size):
    init_val = paper[row][col]
    for i in range(row, row + size):
        for j in range(col, col + size):
            if paper[i][j] != init_val:
                next_size = size // 3
                for x in range(3):
                    for y in range(3):
                        divide(row + x * next_size, col + y * next_size, next_size)
                return
    result[init_val] += 1

divide(0, 0, n)

for v in result.values():
    print(v)