from itertools import combinations

def solution(numbers):
    answer = set()
    [answer.add(sum(i)) for i in list(combinations(numbers, 2))]

    return sorted(answer)

print(solution([2,1,3,4,1]))