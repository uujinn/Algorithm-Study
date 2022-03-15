from sys import stdin

seq = [] # 만들어야하는 수열
stack = []

answer = "" # push, pop 기록
N = int(stdin.readline())

for _ in range(N):
    seq.append(int(stdin.readline()))

index = 0

for i in range(1, N+1):
    stack.append(i) # 일단 stack에 넣고 봅니다.
    answer += '+' # push를 기록합니다.

    # stack이 비어있지 않고, stack 가장 위에 있는 숫자와 만들어야하는 수열의 index번째 숫자와 같다면 계속
    while (stack and stack[-1] == seq[index]): 
        stack.pop() # stack에서 pop 해줌 
        answer += '-' # pop을 기록합니다.
        index += 1 # 해당 숫자 처리했다면 수열에서 다음 숫자 처리할 차례

if stack: # 1 ~ N 숫자 다 사용했는데 아직 stack에 숫자가 남아있다면
    print("no") # 수열 생성 불가
else:
    for i in answer:
        print(i)