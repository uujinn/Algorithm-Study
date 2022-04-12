def solution(s, n):
    answer = ''
    for alpha in s:
        if alpha == ' ':
            answer += alpha
            # continue
        elif 97 <= ord(alpha) < 122 or 65 <= ord(alpha) < 90:
            answer += chr(ord(alpha) + n)
        # elif ord(alpha) + n >= ord('z') or ord(alpha) + n >= ord('Z'):
        #     answer += chr(ord(alpha) + n - 26)
            # continue
        else:
            answer += chr(ord(alpha) + n - 26)
    return answer


# print(solution("AaZz", 25))  # ZzYy
# print(solution("a    b", 1))  # b    c
print(solution("a b ", 1))  # b c
print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
