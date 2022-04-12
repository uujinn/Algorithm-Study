def solution(s, n):
    answer = ''
    for alpha in s:
        if alpha == ' ':
            answer += alpha
            continue
        elif alpha == 'z' or alpha == 'Z':
            answer += chr(ord(alpha) + n - 26)
            continue
        answer += chr(ord(alpha) + n)
    return answer


print(solution("AaZz", 25))  # ZzYy
# print(solution("a    b", 1)) #b    c
# print(solution("a b ", 1) #b c
