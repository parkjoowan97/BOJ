#3130 붙인드롬
import sys
from itertools import product
input = sys.stdin.readline
N , M = map(int,input().split())

#2m 짝수자리의 palin
def palin_even(m):
    palin_list = []
    for palin in product(range(0,10),repeat = m):
        palin = list(palin)
        mirror = palin[::-1]
        palin = palin + mirror
        palin_list.append(palin)
    return palin_list

#2m-1 홀수자리의 palin 
def palin_odd(m):
    palin_list = []
    for palin in product(range(0,10),repeat = m):
        palin = list(palin)
        mirror = palin[::-1]
        mirror.remove(mirror[0])
        palin = palin + mirror
        palin_list.append(palin)
    return palin_list
 
if N % 4 == 0:
    A = palin_even(N//4)
    #앞자리가 0이 아닌 팰린드롬
    palin_1 = [0] * M
    #10^(N//2)로 나눈 나머지를 보존#
    palin_11 = [0] * M
    #앞자리가 0일수도있는 팰린드롬
    palin_2 = [0] * M
    for a in A:
        if a[0] != 0:
            b = "".join(str(s) for s in a)
            b = int(b) % M
            palin_1[b] += 1
            c = ((int(b) % M) * ((10 ** (N//2)) % M)) % M
            palin_11[c] += 1
        else:
            b = "".join(str(s) for s in a)
            b = int(b) % M
            palin_2[b] += 1
    cnt = 0
    for i in range (1,M):
        cnt += palin_11[i] * (palin_1[M-i] + palin_2[M-i])
    cnt += palin_11[0] * (palin_1[0] + palin_2[0])
    print(cnt)
else:
    A = palin_odd(int(N//4)+1)
    #앞자리가 0이 아닌 팰린드롬
    palin_1 = [0] * M
    #10^(N//2)로 나눈 나머지를 보존#
    palin_11 = [0] * M
    #앞자리가 0일수도있는 팰린드롬
    palin_2 = [0] * M
    for a in A:
        if a[0] != 0:
            b = "".join(str(s) for s in a)
            b = int(b) % M
            palin_1[b] += 1
            c = ((int(b) % M) * ((10 ** (N//2)) % M)) % M
            palin_11[c] += 1
        else:
            b = "".join(str(s) for s in a)
            b = int(b) % M
            palin_2[b] += 1
    cnt = 0
    for i in range (1,M):
        cnt += palin_11[i] * (palin_1[M-i] + palin_2[M-i])
    cnt += palin_11[0] * (palin_1[0] + palin_2[0])
    print(cnt)