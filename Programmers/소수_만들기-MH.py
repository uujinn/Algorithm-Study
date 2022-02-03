from itertools import combinations

def is_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
                
    return True

def solution(nums):
    answer = 0
    
    for c in list(combinations(nums, 3)):
        num = c[0] + c[1] + c[2]
        
        if is_prime_number(num):
            answer += 1

    return answer

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))