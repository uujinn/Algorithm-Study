def solution(new_id):
    #step 1
    step_1_answer = list(new_id.lower()) #소문자로 다 변경
    
    #step 2 & 3
    special_char = {"-":1, "_":1, ".":1} #딕셔너리 형태로 사용할 수 있는 특수문자들을 정의해두었음
    answer = [] #step1 -> step2&3 결과를 여기에 저장
    behind_letter = "" #step1의 결과를 뒤에서부터 pop할 것이기 때문에, special_char의 현위치 입장에서 원래는 바로 뒤에 있던 글자를 뜻함.
    
    while len(step_1_answer) != 0:
        popped = step_1_answer.pop()
        
        if popped in special_char or popped.isalpha() or popped.isalnum(): #special_char 딕셔너리 내에 존재하는 특수문자이고, 알파벳이며, 숫자일때
            if popped == '.' and behind_letter == '.': continue #step3 를 함께 처리 하기위해 추가한 조건. 직전에 popped 된 문자가 '.'이라면 pop한 글자를 answer에 추가할 필요가 없음.
            else: answer.append(popped)
        
        behind_letter = answer[-1] if len(answer) != 0 else "" #바로 직전에 answer에 추가한 문자를 새로운 behind_letter로 지정
        
    answer.reverse()#pop한 것들을 추가한 것이기 때문에 거꾸로 되어있음. 다시 원래대로 돌려줌.
    
    #step 4
    if len(answer) > 1:    
        if answer[0] == '.': answer.pop(0)
        if answer[-1] == '.': answer.pop()
    elif len(answer) == 1:
        if answer[0] == '.': answer.pop() #인덱스 에러 방지 위해 추가
        
    
    #step 5
    if len(answer) == 0: answer.append("a") 
    
    #step 6
    answer = answer[0:15] if len(answer) >= 16 else answer #만약 길이가 16이 넘으면 슬라이싱
    if answer[-1] == '.': answer.pop()
    
    #step 7
    if len(answer) < 3: 
        answer.append(answer[-1] * (3 - len(answer))) #3 - answer길이만큼 뺀 값을 곱한 만큼 마지막 문자를 추가함.
    
    return ''.join(answer) #string으로 반환