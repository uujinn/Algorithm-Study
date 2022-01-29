def solution(lottos, win_nums):
    answer = [0, 0]
    unknown = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            answer[1] += 1
        elif lotto == 0:
            unknown += 1
            
    answer[0] = 7 - (answer[1] + unknown)
    answer[1] = 7 - answer[1]
    
    if answer[0] > 6:
        answer[0] = 6
    if answer[1] > 6:
        answer[1] = 6
    
    return answer   # 최고 순위, 최저 순위

print(solution(	[0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))