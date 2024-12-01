N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
same_class_counts = [0] * N

for i in range(N):
    classmates = set()
    for j in range(N):
        if i == j:
            continue
        for k in range(5):
            if classes[i][k] == classes[j][k]:
                classmates.add(j)
                break
    same_class_counts[i] = len(classmates)

max_count = max(same_class_counts)
print(same_class_counts.index(max_count) + 1)