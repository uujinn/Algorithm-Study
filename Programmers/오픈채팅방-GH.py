def solution(record):
    answer = []
    dic = {}

    for command in record:
        command_ = command.split()
        if len(command_) == 3:
            dic[command_[1]] = command_[2]

    for command in record:
        command_ = command.split()
        if command_[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % dic[command_[1]])
        elif command_[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % dic[command_[1]])

    return (answer)