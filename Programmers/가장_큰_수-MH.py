from functools import cmp_to_key

def compare(a, b):
    x = int(a + b)
    y = int(b + a)
    
    if x == y:
        return 0
    elif x > y:
        return 1
    elif x < y:
        return -1
    

def solution(_numbers):
    numbers = [str(n) for n in _numbers]
    numbers.sort(key=cmp_to_key(compare), reverse=True)
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))