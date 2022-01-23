def solution(board, moves):
    answer = 0
    bucket = []
    
    for move in moves:
        for line in board:
            if line[move-1] != 0:
                bucket.append(line[move-1])
                line[move-1] = 0
                break

        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            answer += 2
            bucket = bucket[:-2]
            
    return answer