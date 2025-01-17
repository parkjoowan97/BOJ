pow_two = [2 ** i for i in range (0, 31)]
N = int(input())
if N in pow_two:
    print(1)
else:
    print(0)