def solution(s):
    answer = ''
    i = 0
    
    for char in s:
        if char == ' ':
            answer += ' '
            i = 0
            continue
        
        if i % 2 == 0:
            answer += char.upper()
        else:
            answer += char.lower()
        i += 1
    
    if len(s) != len(answer):
        answer += s[:len(s) - len(answer)]
    return answer

print(solution("try hello world"))