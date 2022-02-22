def solution(n):
    sol = ''
    
    while n >= 1:               # 10진법 -> 앞뒤 반전한 3진법
        temp = divmod(n, 3)     # n을 3으로 나눈 몫, n을 3으로 나눈 나머지 반환
        n = temp[0]
        sol += str(temp[1])     # 나머지 더해줌

    return int(sol, base = 3)

print(solution(45))