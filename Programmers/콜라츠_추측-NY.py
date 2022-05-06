def solution(num):
    cnt = 0
    while True:
        if num == 1: return cnt
        if cnt >= 500: return -1
        if not num % 2: num//= 2
        else: num = num * 3 + 1
        cnt += 1