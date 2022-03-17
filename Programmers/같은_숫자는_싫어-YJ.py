def solution(arr):
    answer = []
    x_value = -1
    for idx, val in enumerate(arr):
        if idx == 0:
            answer.append(val)
            x_value = val
            continue
        if x_value != val:
            answer.append(val)
        x_value = val

    return answer

print(solution([4,4,4,3,3]))