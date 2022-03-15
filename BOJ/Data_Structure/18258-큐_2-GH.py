from sys import stdin

input() # 명령 받기

q, command= [], stdin.readlines()
cnt = 0     # 가장 앞의 index 값을 저장하는 변수

for i in command:
    x = i.split()
    
    if x[0] == "push":
        q.append(x[1])
    elif x[0] == 'pop':
        if len(q) > cnt:
            print(q[cnt])
            cnt += 1
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(q)-cnt)
    elif x[0] == 'empty':
        if len(q) == cnt :
            print(1)
            cnt = 0
            q = []
        else:
            print(0)
    elif x[0] == 'front':
        if len(q) > cnt:
            print(q[cnt])
        else: 
            print(-1)
    elif x[0] == 'back':
        if len(q) > cnt: print(q[-1])
        else: 
            print(-1)