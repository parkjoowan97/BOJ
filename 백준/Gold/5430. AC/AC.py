import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range (T):
    cmd = input().strip()
    n = int(input())
    input_str = input().strip()
    num = list(map(str, input_str.strip('[]').split(',')))
    if num == [""]:
        deq = deque()
    else:
        deq = deque(num)
    direction = True #정방향
    cnt = 0
    for command in cmd:
        if command == "R":
            if direction == True:
                direction = False
            else:
                direction = True
        else:
            cnt += 1
            if direction == True:
                if len(deq) == 0:
                    print("error")
                    break
                deq.popleft()
            else:
                if len(deq) == 0:
                    print("error")
                    break
                deq.pop()
    if cnt < n:
        ans = list(deq)
        if direction == False:
            ans = ans[::-1]
        answer = ",".join(string for string in ans)
        answer = "[" + answer + "]"
        print(answer)
    if cnt == n:
        print("[]")