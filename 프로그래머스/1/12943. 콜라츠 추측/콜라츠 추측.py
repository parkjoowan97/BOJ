def solution(num):
    cnt = 0
    if num == 1:
        return 0
    while True:
        cnt += 1
        if cnt == 501:
            return -1
        else:
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
        if num == 1:
            break
    return cnt