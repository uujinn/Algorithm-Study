from sys import stdin

def is_right_bracket(bracket):                      # 올바른 괄호열인지 계싼
    stack = []
    
    for b in bracket:
        if b in '([':
            stack.append(b)
        elif b in ')]':
            if not stack:
                return False
            if stack[-1] == '(' and b == ')':
                stack.pop()
            elif stack[-1] == '[' and b == ']':
                stack.pop()
    
    return False if stack else True
      

def bracket_value(bracket : str) -> int:
    print('recur')
    answer = 0
    match_index = 0                                 # 시작하는 괄호의 짝을 찾는 index
            
    value = 2 if bracket[0] == '(' else 3           # 시작하는 괄호가 '(' -> 2, '[' -> 3
    
    for i, b in enumerate(bracket):
        if b == '(' or b == '[':
            match_index += 1
        else:
            match_index -= 1
        
        if match_index == 0:                        # 시작하는 괄호의 짝을 찾음
            if i == 1 and i == len(bracket) - 1:                    # () 또는 []인 경우
                return value
              
            elif i == 1 and i != len(bracket) - 1:                  # left : () or [], right 존재
                answer += (value + bracket_value(bracket[2:]))
                break
            
            elif i == len(bracket) - 1:             # 짝 괄호가 맨 마지막에 위치하면
                answer += (bracket_value(bracket[1:-1]) * value)
                break
                
            else:
                left = bracket[:i + 1]
                right = bracket[i + 1:]             # 오른쪽                
                answer += (bracket_value(left) + bracket_value(right))
                break
                    
    return answer
        
bracket = stdin.readline().rstrip()
print(bracket_value(bracket) if is_right_bracket(bracket) else 0)