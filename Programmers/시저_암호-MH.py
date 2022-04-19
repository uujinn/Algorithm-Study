def solution(s, n):
    answer = ''
    
    for char in s:
        if char == ' ':
            answer += ' '
            continue
        
        if char.isupper():
            temp = 65 + ((ord(char) + n - 65) % 26)
        elif char.islower():
            temp = 97 + ((ord(char) + n - 97) % 26)
            
        answer += chr(temp)
    return answer

print(solution("C a Z z Y s", 20))
# W u T t S m