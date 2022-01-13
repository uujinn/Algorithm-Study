def solution(lottos, win_nums):
    answer = []
    count_zero = 0
    count_right = 0
    count_wrong = 0
    
    for i in range(6):
        if lottos[i] == 0:
            count_zero += 1 #0은 wrong, right 경우의 수를 결정해주기 때문에 따로 count
        for j in range(6):
            if lottos[i] == win_nums[j]: count_right += 1 #정답인 경우만 따로 count
    
    count_wrong = 6 - count_right - count_zero
    
    answer.append(7 - count_right - count_zero if count_wrong != 6 else 6) #7 - 맞은 갯수 - 0인 갯수의 최대값 = 등수.
    #만약 count_wrong == 6 이면 다 틀렸다는 뜻으로, 최악의 등수가 6등이므로 거기에 맞출 수 있도록 else 6 으로 조건 추가
    
    answer.append(7 - count_right if count_right != 0 else 6) #7 - 맞은 갯수
    return answer
