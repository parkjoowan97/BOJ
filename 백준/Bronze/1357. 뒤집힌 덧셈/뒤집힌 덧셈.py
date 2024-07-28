A,B = map(str,input().split())
answer = int(str(int(A[::-1]) + int(B[::-1]))[::-1])
print(answer)