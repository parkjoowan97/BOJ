K = int(input())
directions = []
lengths = []
for _ in range(6):
    d, l = map(int, input().split())
    directions.append(d)
    lengths.append(l)

max_width, max_width_idx = 0, -1
max_height, max_height_idx = 0, -1

for i in range (0, 6):
    if directions[i] in [1,2]:
        if lengths[i] > max_width:
            max_width = lengths[i]
            max_width_idx = i
    elif directions[i] in [3,4]:
        if lengths[i] > max_height:
            max_height = lengths[i]
            max_height_idx = i

small_width = lengths[(max_width_idx + 3) % 6]
small_height = lengths[(max_height_idx + 3) % 6]

print(((max_width * max_height) - (small_width * small_height)) * K)