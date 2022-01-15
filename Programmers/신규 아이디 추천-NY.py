def solution(new_id):
    #step 1
    step_1_answer = list(new_id.lower())
    
    #step 2 & 3
    special_char = {"-":1, "_":1, ".":1}
    answer = []
    behind_letter = ""
    
    while len(step_1_answer) != 0:
        popped = step_1_answer.pop()
        
        if popped in special_char or popped.isalpha() or popped.isalnum():
            if popped == '.' and behind_letter == '.': continue
            else: answer.append(popped)
        
        behind_letter = answer[-1] if len(answer) != 0 else ""
        
    answer.reverse()
    
    #step 4
    if len(answer) > 1:    
        if answer[0] == '.': answer.pop(0)
        if answer[-1] == '.': answer.pop()
    elif len(answer) == 1:
        if answer[0] == '.': answer.pop()
        
    
    #step 5
    if len(answer) == 0: answer.append("a") 
    
    #step 6
    answer = answer[0:15] if len(answer) >= 16 else answer
    if answer[-1] == '.': answer.pop()
    
    #step 7
    if len(answer) < 3: 
        answer.append(answer[-1] * (3 - len(answer)))
    
    return ''.join(answer)