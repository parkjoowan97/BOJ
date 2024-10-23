from collections import defaultdict
N = int(input())
names = defaultdict(list)
for _ in range (0,N):
    a = input()
    names[a[:1]].append(a)

name_tuple = names.items()
answer = []
for ini, name_list in name_tuple:
    if len(name_list) >= 5:
        answer.append(ini)

answer.sort()
if len(answer) == 0:
    print("PREDAJA")
else:
    print("".join(str(s) for s in answer))