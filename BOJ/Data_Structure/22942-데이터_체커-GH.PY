import sys
input = sys.stdin.readline


class dataChecker:
    def __init__(self, point, isOpen, yn):
        self.point = point
        self.isOpen = isOpen
        self.yn = yn


def solution(N):
    circles = []

    for i in range(N):
        x, r = map(int, input().split())

        circles.append(dataChecker(x - r, True, i))  # == 여는 괄호
        circles.append(dataChecker(x + r, False, i))  # == 닫는 괄호

    circles.sort(key=lambda x: x.point)
    stack = []
    meet = set()
    for circle in circles:
        next = circle
        if next.point in meet:  # 내외접
            print("NO")
            return
        if next.isOpen:
            stack.append(next)
            meet.add(next.point)
        elif stack[-1].yn != next.yn:  # 교차
            print("NO")
            return
        else:
            meet.add(next.point)
            stack.pop()
    print('YES')


if __name__ == "__main__":
    N = int(input())
    solution(N)