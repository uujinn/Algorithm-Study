from collections import Counter

def solution(participant, completion):
    count = Counter(participant) - Counter(completion)
    return list(count.keys()).pop()