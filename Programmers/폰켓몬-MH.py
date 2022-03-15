def solution(nums):
    return int(len(nums) / 2) if len(nums) / 2 <= len(set(nums)) else len(set(nums))

print(solution([3,3,3,2,2,2]))