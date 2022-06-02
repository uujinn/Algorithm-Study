def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min_number = min(arr)
        for n in arr:
            if n == min_number:
                arr.remove(n)
                return arr


print(solution([4, 3, 2, 1]))
