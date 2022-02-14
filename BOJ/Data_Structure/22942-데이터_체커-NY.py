from sys import stdin
N = int(stdin.readline())
circles = []
stack = []
for _ in range(N):
    x, r = map(int, stdin.readline().split())
    circles.append([x-r, x+r]) #각 원의 왼쪽 끝점과 오른쪽 끝점을 저장
    
for circle in sorted(circles): #sorted를 통해 왼쪽 점들 기준으로 정렬. 가장 왼쪽에 가까운 점들부터 처리.
    if not stack: stack.append(circle) #만약 스택이 비어있으면(처음이면) 추가
    else:
        #circle이 스택 가장 위에 있는 놈이랑 비교했을때 위에 놈 [왼, 오] 사이에 들어가거나, 위에 놈 오른쪽보다 circle의 왼,오가 다 커야됨.
        if (circle[0] > stack[-1][0] and circle[1] < stack[-1][1]) or (circle[0] > stack[-1][1] and circle[1] > stack[-1][1]): 
            stack.append(circle)
        else:
            print("NO")
            exit()
            
print("YES")