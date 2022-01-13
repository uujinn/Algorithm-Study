def solution(lottos, win_nums):
    answer = []

    set_lottos = set(lottos)
    set_win = set(win_nums)
    
    # 교집합으로 겹치는 요소 파악
    same_num = len(set_lottos & set_win)
    invisible_num = lottos.count(0)
    
    highest_rank = 7 - (same_num + invisible_num)
    lowest_rank = 7 - same_num
    
    # etc 
    if highest_rank == 7:
        highest_rank = 6

    if lowest_rank == 7:
        lowest_rank = 6
    
    answer.append(highest_rank)
    answer.append(lowest_rank)
    
    return answer
