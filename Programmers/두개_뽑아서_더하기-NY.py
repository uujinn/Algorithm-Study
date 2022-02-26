from itertools import combinations
def solution(numbers):
    answer = set()
    for number in list(combinations(numbers, 2)): 
        if number[0] + number[1] not in answer: answer.add(number[0] + number[1])
    return sorted(list(answer))