def solution(nums):
    nums = sorted(nums) #정렬
    temp = nums[0]
    answer = 1
    for i in range(1, len(nums)):
        if nums[i] != temp: #같은건 포함 의미가 없으니까 같지 않을때만 count
            answer += 1 
            temp = nums[i]
    return answer if answer <= len(nums)//2 else len(nums)//2 #N/2가 최댓값이니 마지막에 비교