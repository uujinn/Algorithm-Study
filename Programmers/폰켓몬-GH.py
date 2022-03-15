def solution(nums):
       
    answer = 0
    N = len(nums)//2
    num_set = list(set(nums))

    if len(num_set) > N:
        answer = N
       
    else:
        answer = len(num_set)
       
    return answer