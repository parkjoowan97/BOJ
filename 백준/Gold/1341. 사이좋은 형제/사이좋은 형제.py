import math
a,b = map(int,input().split())

def f(a,b):
    if a == 0 and b == 0:
        return -1
    elif a == 0 and b != 0:
        return "-"
    elif a == 1 and b == 1:
        return "*"
    #이제 비트마스킹을 활용해야함
    else:
        for i in range (1,64):
            t = a * ((2 ** i) - 1) // b
            if b * t == a * ((2 ** i) - 1):
                x = format(t, 'b') #주어진 숫자를 2진수로 변환해야할 필요가 있음
                if i >= len(x):
                    new_x = "0" * (i - len(x)) + x
                    ans = ""
                    for j in range (0,i):
                        if new_x[j] == "0":
                            ans += "-"
                        else:
                            ans += "*"
                    if len(ans) >= 61:
                        return -1
                    return ans
        return -1
print(f(a,b))