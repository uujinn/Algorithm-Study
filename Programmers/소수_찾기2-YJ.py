from itertools import permutations
import math


def isPrime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    numbers = str(numbers)
    num_arr = list(map(int, list(numbers)))

    answer = []
    cnt = 0

    for i in range(len(num_arr)):
        # print(set(list("".join(permutations(num_arr, i+1)))))
        permutation = list((permutations(num_arr, i+1)))
        for p in permutation:
            tmp = ''
            for q in p:
                tmp += str(q)
            answer.append(int(tmp))

    answer = set(answer)

    for i in answer:
        if isPrime(i):
            cnt += 1

    return cnt


print(solution("011"))
