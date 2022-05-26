def solution(record):
    users = {}
    answer = []
    for re in record:
        try: cmd, i_d, name = re.split(' ')
        except: cmd, i_d = re.split(' ')
        if cmd == "Enter" or cmd == "Change":
            users[i_d] = name
    for re in record:
        try: cmd, i_d, name = re.split(' ')
        except: cmd, i_d = re.split(' ')
        if cmd == "Enter":
            answer.append("%s님이 들어왔습니다." %users[i_d])
        elif cmd == "Leave":
            answer.append("%s님이 나갔습니다." %users[i_d])
    return answer