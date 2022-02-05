def solution(participant, completion):
    participant.sort()
    completion.sort()

    for par, com in zip(participant, completion):
        if par != com:
            return par
    return participant[-1]
        

print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
print(solution(["mislav", "ana", "ana", "ana"],	["mislav", "ana", "ana"]))