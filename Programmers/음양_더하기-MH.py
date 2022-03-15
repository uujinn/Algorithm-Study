def solution1(absolutes, signs):
    for i in range(len(absolutes)):
        if not signs[i]: absolutes[i] *= -1
    return sum(absolutes)

def solution2(absolutes, signs):
    answer = 0
    for idx, num in enumerate(absolutes):
        answer = answer + num if signs[idx] else answer - num
    return answer

print(solution2([1,2,3],	[False,False,True]))