def solution(arr):
    answer = []
    for i in range(len(arr)):
        if answer and arr[i-1] == arr[i]: continue
        else: answer.append(arr[i])
    return answer
