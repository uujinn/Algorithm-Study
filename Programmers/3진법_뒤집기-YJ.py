def getTernary(x): # 앞 뒤 반전된 3진법 구하기
    answer = ""
    while x > 0:
        answer += str(x % 3)
        x //= 3
        if 0 < x < 3:
            answer += str(x)
            break
    return answer

def solution(n):
    answer = int(getTernary(n), 3) # 3진법으로 바꿔줌
    return answer

print(solution(45))