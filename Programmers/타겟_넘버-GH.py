answer = 0

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer

def dfs(idx, numbers, target, value):
    global answer

    length = len(numbers)

    if(idx == length and target == value):
        answer += 1
        return
    if(idx == length):
        return

    dfs(idx+1, numbers, target, value+numbers[idx])
    dfs(idx+1, numbers, target, value-numbers[idx])