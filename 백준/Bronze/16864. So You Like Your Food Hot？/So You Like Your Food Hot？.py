p_t,p_1,p_2 = map(float,input().split())
p_t = int(round(p_t * 100,1))
p_1 = int(round(p_1 * 100,1))
p_2 = int(round(p_2 * 100,1))
k = p_t // p_1

ans = []
for i in range (0,k+1):
    if (p_t - i * p_1) % p_2 == 0:
        ans.append([i, (p_t - i * p_1) // p_2])
if ans == []:
    print("none")
else:
    for answer in ans:
        print(" ".join(str(s) for s in answer))