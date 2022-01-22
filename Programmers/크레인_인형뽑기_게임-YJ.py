from collections import deque

def solution(board, moves):
    
    answer = 0
    basket = deque([])

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0: # index = move-1
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                break
            
            if len(basket) > 1: 
                if basket[len(basket)-1] == basket[len(basket)-2]: # 인형 겹치면 둘 다 OUT
                    basket.popleft()
                    basket.popleft()
                    answer += 2
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))