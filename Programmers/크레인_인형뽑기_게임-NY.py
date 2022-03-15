from more_itertools import bucket


def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                if len(basket) != 0 and basket[-1] == board[i][move-1]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[i][move-1])
                board[i][move-1] = 0
                break

    return answer