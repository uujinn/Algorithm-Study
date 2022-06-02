def solution(x):
    arr = map(int, list(str(x)))

    if x % sum(arr) == 0:
        return True
    else:
        return False


print(solution(18))
