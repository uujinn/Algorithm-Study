from sys import stdin
n = int(stdin.readline())
stack = [] #스택 저장
seq = [] #만들어야 하는 수열 저장
answer = [] #+,- 저장
cnt = 0 #오름차순으로 숫자 더해서 stack에 넣어줄 숫자
for i in range(n):
    seq.append(int(stdin.readline()))

for s in seq:
    while not len(stack) or s != stack[-1]: #길이가 0이거나 수열값과 스택 마지막 값이 같지 않을때 반복
        if len(stack) and stack[-1] > s: #스택 마지막 값이 수열값보다 클때
            print("NO")
            exit()
        elif not len(stack) or stack[-1] < s: #스택 길이가 0이거나 스택 마지막 값이 수열값보다 작을때
            cnt += 1
            answer.append("+")
            stack.append(cnt)
    
    #s == stack[-1]. while문이 끝나면 무조건 둘의 값은 같음
    answer.append("-")
    stack.pop()
    
for a in answer:
    print(a)