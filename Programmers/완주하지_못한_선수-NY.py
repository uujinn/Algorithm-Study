def solution(participant, completion):
    participant_s = sorted(participant)
    for i, (p, c) in enumerate(zip(participant_s, sorted(completion))):
        if p != c: return p
        elif i == len(completion) - 1: return participant_s[-1]