from sys import stdin

q = []
num = int(stdin.readline())

for i in range(num):
    str = stdin.readline().split()
    
    if str[0] == 'push':
        q.append(str[1])
    elif str[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.remove(q[0])
    elif str[0] == 'size':
        print(len(q))
    elif str[0] == 'empty':
        print(1 if len(q) == 0 else 0)
    elif str[0] == 'front':
        print(q[0] if len(q) > 0 else -1)
    elif str[0] == 'back':
        print(q[-1] if len(q) > 0 else -1)