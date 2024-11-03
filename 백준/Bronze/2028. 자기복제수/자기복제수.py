T = int(input())
for _ in range (T):
    a = int(input())
    squared_a = str(a ** 2)
    n = len(str(a))
    if squared_a[-n:] == str(a):
        print("YES")
    else:
        print("NO")