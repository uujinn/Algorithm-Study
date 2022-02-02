import math
from itertools import combinations

def isPrime(x): # 소수 판별
    for i in range(2, int(math.sqrt(x)) + 1): # x의 약수는 x를 제외한 x의 제곱근이 최대
        if x % i == 0:
            return False # 소수 X
    return True # 소수 O

def solution(nums):
    answer = 0

    combi_result = list(combinations(nums, 3)) # 조합

    for i in range(len(combi_result)):
        if isPrime(sum(combi_result[i])):
            answer += 1

    return answer
