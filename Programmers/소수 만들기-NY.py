from itertools import combinations
import math
def solution(nums):
    answer = 0
    flag = False 
    added_nums = list(combinations(nums, 3))
    
    for num in added_nums:
        added = num[0] + num[1] + num[2]
        for i in range(2, int(math.sqrt(added)) + 1):
            if added % i == 0: 
                flag = False
                break
            else: flag = True
        
        if flag: answer += 1
            
    return answer

print(solution([1,2,7,6,4]))