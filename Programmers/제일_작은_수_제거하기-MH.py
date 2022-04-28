from array import ArrayType


def solution(arr):
    arr.remove(min(arr))
    return arr

print(solution  ([4, 3, 2, 1]))