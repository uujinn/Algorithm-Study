from itertools import permutations

def isPrime(x):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    num = []

    for i in range(1, len(numbers)+1):
        num.append(list(set(map(''.join, permutations(numbers, i)))))

    results = list(set(map(int, set(sum(num, [])))))

    for j in results:
        if isPrime(j) == True:
            answer += 1

    return answer