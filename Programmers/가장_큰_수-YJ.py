from functools import cmp_to_key


def keyForLambda(a, b):
    x = a + b
    y = b + a

    if x == y:
        return 0
    elif x > y:
        return 1
    elif x < y:
        return -1


def solution(numbers):

    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(keyForLambda), reverse=True)
    return str(int(''.join(numbers)))


print(solution([3, 30, 34, 5, 9]))
