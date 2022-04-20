def solution(s, n):
    answer = ''
    for alpha in s:
        if alpha == ' ':
            answer += alpha
            # continue
        elif 65 <= ord(alpha) < 90:
            plus = ord(alpha) + n
            if plus > 90:
                plus -= 26
            answer += chr(plus)
        elif 97 <= ord(alpha) < 122:
            plus = ord(alpha) + n
            if plus > 122:
                plus -= 26
            answer += chr(plus)
        else:
            answer += chr(ord(alpha) + n - 26)
    return answer


# print(solution("AaZz", 25))  # ZzYy
# print(solution("a    b", 1))  # b    c
# print(solution("a b ", 1))  # b c
print(solution("a", 4))  # e F d
