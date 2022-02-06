from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).elements()).pop()
        

print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
print(solution(["mislav", "ana", "ana", "ana"],	["mislav", "ana", "ana"]))