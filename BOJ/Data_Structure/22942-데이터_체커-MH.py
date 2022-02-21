import sys

class Circle:
    def __init__(self, no, pos, is_open):
        self.no, self.pos, self.is_open = no, pos, is_open

circles, stack, marked = [], [], set()

for i in range(int(sys.stdin.readline().rstrip())):
    x, r = map(int, sys.stdin.readline().split())
    circles.append(Circle(i, x - r, True))         # 원의 시작 점
    circles.append(Circle(i, x + r, False))        # 원의 끝 점

circles.sort(key = lambda x : x.pos)

for c in circles:
    if c.pos in marked:                # 점이 겹칠 때
        print('NO')
        sys.exit(0)
        
    if c.is_open:                      # 원의 시작 점일 때 stack에 추가
        stack.append(c)
        marked.add(c.pos)              # 자리 찜꽁
    else:                              # 원의 끝 점 일 때
        if stack[-1].no == c.no:
            stack.pop()
            marked.add(c.pos)
        else:
            print('NO')
            sys.exit(0)
    
print('YES')

# 1020ms