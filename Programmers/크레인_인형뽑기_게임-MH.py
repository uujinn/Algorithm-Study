from collections import deque

answer = 0

def append_basket(basket, num):
    global answer
    
    if len(basket) > 0 and basket[-1] == num:
        basket.pop()
        answer += 2
    else:
        basket.append(num)

def solution(board, moves):
    global answer
    basket = deque()

    for i in moves:
        for j in range(len(board)):
            doll = board[j][i - 1]   # 크레인이 집은 인형

            if not doll == 0:
                append_basket(basket, doll)
                board[j][i - 1] = 0
                break

    return answer   #  크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))