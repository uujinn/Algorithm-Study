def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def solution(n, m):
    answer = []
    
    if n < m: n, m = m, n
    answer.append(GCD(n, m))                # 최대공약수
    answer.append(n * m // answer[0])       # 최소공배수
    
    return answer

print(solution(3, 12))