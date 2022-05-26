from collections import defaultdict


def solution(record):
    answer = []

    userDB = defaultdict()
    actions = []

    for r in record:
        r = r.split()
        if r[0] == 'Leave':
            actions.append((r[0], r[1]))
        else:
            userDB[r[1]] = r[2]  # 그 시점 최신 이름 갱신
            actions.append((r[0], r[1]))

    for action in actions:
        if action[0] == 'Enter':
            answer.append(f'{userDB[action[1]]}님이 들어왔습니다.')
        elif action[0] == 'Leave':
            answer.append(f'{userDB[action[1]]}님이 나갔습니다.')
        else:  # Change 일 때
            continue

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
