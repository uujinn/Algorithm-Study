from sys import stdin
from itertools import combinations

class Circle:
    def __init__(self, x, r):
        self.x = x
        self.r = r
        
def data_check(circle_1, circle_2):
    d = abs(circle_1.x - circle_2.x)        # 두 원의 중심 사이 거리
    
    if circle_1.r + circle_2.r < d or abs(circle_1.r - circle_2.r) > d:
        return True
    return False

circles = []
check = True

for _ in range(int(stdin.readline().rstrip())):
    x, r = map(int, stdin.readline().split())
    circles.append(Circle(x, r))

for com_1, com_2 in combinations(circles, 2):
    if not data_check(com_1, com_2):
        check = False
        break