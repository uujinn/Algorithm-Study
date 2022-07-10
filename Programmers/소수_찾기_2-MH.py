from itertools import permutations

def is_prime(n):
    if n in ["", "0", "1"]:
        return False
    
    n = int(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    

def solution(_numbers):
    num = [_numbers[i] for i in range(len(_numbers))]
    # print(num)
    # num : ['0', '1', '1']
    
    numbers = set()
    for i in range(1, len(_numbers) + 1):
        for per in permutations(num, i):
            temp = ""
            
            for p in per:
                temp += p                
            numbers.add(temp.lstrip("0"))
            
    # print(numbers)
    # numbers : {'', '1', '110', '10', '11', '101'}
    
    answer = 0
    for n in numbers:
        if is_prime(n):
            # print(n)
            answer += 1
    
    return answer

print(solution("011"))