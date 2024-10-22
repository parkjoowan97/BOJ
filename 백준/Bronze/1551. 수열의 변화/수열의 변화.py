N, K = map(int,input().split())
number = list(map(int,input().split(",")))
cnt = 0
while cnt != K:
    new_number = []
    for i in range (0,len(number)-1):
        new_number.append(number[i+1] - number[i])
    cnt += 1
    number = new_number
print(",".join(str(s) for s in number))