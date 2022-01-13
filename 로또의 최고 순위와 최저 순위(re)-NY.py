def solution(lottos, win_nums):
    answer = []
    
    rank = [6,6,5,4,3,2,1] #0개 맞았을때부터 6개 맞았을때까지 임의의 rank배열 생성
    count_zero = 0
    count_right = 0
    
    for i in range(6):
        if lottos[i] == 0:
            count_zero += 1
        for j in range(6):
            if lottos[i] == win_nums[j]: count_right += 1
                
    answer.append(rank[count_right + count_zero]) #배열 값을 append
    answer.append(rank[count_right])
    
    return answer
  
  #처음에 했던것보다 마지막 과정이 단순함
