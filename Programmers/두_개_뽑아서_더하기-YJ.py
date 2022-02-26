import itertools

def solution(numbers):
    arr = list(itertools.combinations(numbers, 2))
    answer = [0] * len(arr)
    for i in range(len(arr)):
        answer[i] = sum(arr[i])

    answer = sorted(list(set(answer)))
    return answer