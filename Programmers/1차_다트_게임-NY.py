def solution(dartResult):
    calculate = {"S": 1, "D": 2, "T": 3}
    bonus = {"*": 2, "#": -1}
    scores = []
    answers = []
    before_idx = 0
    for i, d in enumerate(dartResult): #숫자들을 찾아서 그 앞까지 슬라이싱할 인덱스 저장하려고 돌린 for문
        if d.isalnum() and before_idx != i and before_idx + 1 != i and dartResult[i-1] != '0':
            scores.append(dartResult[before_idx: i])
            before_idx = i
    scores.append(dartResult[before_idx:])
    for i, score in enumerate(scores):
        num = int(score[0]) if score[1] != '0' else int(score[0:2]) #점수만 저장
        if score[-1] in bonus: #마지막에 보너스가 있으면
            answers.append(num ** calculate[score[-2]])
            if i == 0 and score[-1] == '*': answers[-1] *= 2
            elif i and score[-1] == '*': 
                answers[-2] *= 2
                answers[-1] *= 2
            elif score[-1] == "#": answers[-1] *= -1
        else: #보너스 없으면
            answers.append(num ** calculate[score[-1]])
    return sum(answers)