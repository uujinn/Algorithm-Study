from sys import stdin
N = int(stdin.readline())
towers = list(enumerate(map(int, stdin.readline().split()))) #인덱스를 함꼐 저장
answers = [0 for i in range(N)] #갯수만큼 answer에 0미리 저장
stack = [towers[-1]] #스택에 towers 뒤에서부터 넣을거라서 미리 하나 넣어둠

for i in range(N-2, -1, -1): 
    while stack and towers[i][1] > stack[-1][1]: #스택이 비어 있지 않고 towers의 값이 stack의 마지막 인덱스 값보다 클때 계속 반복
        answers[stack.pop()[0]] = towers[i][0]+1 #stack에서 pop한 값의 '인덱스'의 answers에 접근해서 towers의 인덱스 값+1을 저장
    stack.append(towers[i])
    
for a in answers:
    print(a, "", end="")