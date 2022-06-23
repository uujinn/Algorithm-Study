def solution(places):
    answer = []
    #응시자 자리 P 빈 테이블 O 파티션 X
    for p in places:
        for i in range(5): #y
            for j in range(5): #x
                aparted = True
                standard = p[i][j]
                if standard != 'P': continue
                else:
                    #위쪽
                    if i-2 >= 0: 
                        if p[i-1][j] == 'O' and p[i-2][j] == 'P':
                            aparted = False
                            break
                    elif i-1 >= 0:
                        if p[i-1][j] == 'P': 
                            aparted = False
                            break
                    #왼쪽-위쪽 대각선
                    if i-1 >= 0 and j-1 >=0:
                        if (p[i][j-1] == 'O' or p[i-1][j]=='O') and p[i-1][j-1] == 'P':
                            aparted = False
                            break
                    #왼쪽
                    if j-2 >= 0:
                        if p[i][j-1] == 'O' and p[i][j-2] == 'P':
                            aparted = False
                            break
                    elif j-1 >= 0:
                        if p[i][j-1] == 'P':
                            aparted = False
                            break

                    #왼쪽-아래쪽 대각선
                    if i+1 <= 4 and j-1 >= 0:
                        if (p[i+1][j]=='O' or p[i][j-1]=='O') and p[i+1][j-1] == 'P':
                            aparted = False
                            break

                    #아래쪽
                    if i+2 <= 4:
                        if p[i+1][j] == 'O' and p[i+2][j] == 'P':
                            aparted = False
                            break
                    elif i+1 <= 4:
                        if p[i+1][j] == 'P':
                            aparted = False
                            break

                    #아래쪽-오른쪽 대각선
                    if i+1 <=4 and j+1 <=4:
                        if (p[i+1][j] =='O' or p[i][j+1]=='O') and p[i+1][j+1] == 'P':
                            aparted = False
                            break

                    #오른쪽
                    if j+2 <= 4:
                        if p[i][j+1] == 'O' and p[i][j+2] == 'P':
                            aparted=False
                            break
                    elif j+1 <= 4:
                        if p[i][j+1] == 'P':
                            aparted=False
                            break

                    #오른쪽-위쪽 대각선
                    if i-1 >= 0 and j+1 <= 4:
                        if (p[i-1][j]=='O' or p[i][j+1] =='O') and p[i-1][j+1] == 'P':
                            aparted=False
                            break
        if aparted: answer.append(1)
        else: answer.append(0)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))