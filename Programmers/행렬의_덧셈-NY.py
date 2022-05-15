def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        tmp = []
        for x, y in zip(a,b):
            tmp.append(x+y)
        answer.append(tmp)
    return answer