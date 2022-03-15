def solution(lottos, win_nums):
    
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    count = 0
    zero_count = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            count += 1
            
    answer[0], answer[1] = rank[count + zero_count], rank[count]
    
    return answer