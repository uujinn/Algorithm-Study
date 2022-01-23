def solution(board, moves):
    answer = 0
    non_zeros = []
    bucket = []
    #0이 아닌 최초의 값의 인덱스를 non_zeros라는 리스트에 저장해서 moves값에 따라 
    #탐색 없이 바로 board에서 꺼낼 수 있게함.
    
    for i in range(len(board[0])):
        temp = list(filter(lambda x: board[x][i] != 0, range(len(board))))
        if len(temp) == 0: non_zeros.append(len(board)) #해당 열은 모두 0임 
        else: non_zeros.append(temp[0]) 
    
    for move in moves:
        move_index = move - 1
        non_zero_index = non_zeros[move_index]
        if non_zero_index == len(board): #해당 열이 모두 0이라서 뽑을 게 없음
            continue
        else: 
            picked = board[non_zero_index][move_index]
            board[non_zero_index][move_index] = 0 #뽑고 나서 해당 자리의 값을 0으로 변경
            non_zeros[move_index] += 1 #0으로 변경되면서 0이 아닌 인덱스가 한 칸 밀림
            
            if len(bucket) == 0 or bucket[-1] != picked: 
                bucket.append(picked)
            else: #bucket 마지막에 있는 값과 새로 뽑은 값이 일치.
                bucket.pop()
                answer += 2

    return answer