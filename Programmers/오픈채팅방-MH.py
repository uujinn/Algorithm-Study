def solution(record):
    user = {}
    answer, actions = [], []
    
    for r in record:
        temp = list(map(str, r.split()))
        
        actions.append((temp[0], temp[1]))
        if len(temp) == 3:             # Enter, Change
            user[temp[1]] = temp[2]           # id와 닉네임 업데이트

    for action in actions:
        if action[0] == 'Enter':
            answer.append(user[action[1]] + '님이 들어왔습니다.')
        elif  action[0] == 'Leave':
            answer.append(user[action[1]] + '님이 나갔습니다.')
            
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))