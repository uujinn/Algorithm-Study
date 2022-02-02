import math
def solution(nums):
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                added = i + j + k
                for p in range(2, int(math.sqrt(added)) + 1):
                    if added % p == 0: answer += 1
    return answer
