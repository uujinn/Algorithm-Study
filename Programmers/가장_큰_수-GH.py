def solution(numbers):
    nums = [str(n) for n in numbers]
    nums.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(nums)))