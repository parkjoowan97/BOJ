def count_excluded_problems(n, difficulties):
    excluded_count = sum(1 for d in difficulties if d % 2 != 0)
    return excluded_count

n = int(input())
difficulties = [int(input()) for _ in range(n)]

print(count_excluded_problems(n, difficulties))