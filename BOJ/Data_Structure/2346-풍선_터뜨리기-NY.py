from collections import deque
from sys import stdin
from collections import deque

N = int(stdin.readline())
numbers = deque(map(int, stdin.readline().split()))
matches = {}

for i in range(N):
    matches[i+1] = numbers[i] #키: 1부터 N까지의 숫자 / value: 종이에 적혀 있는 숫자
    numbers[i] = i + 1 #1부터 N까지 순서대로 덱에 집어넣음

while numbers:
    wanted = numbers[0]
    print(numbers.popleft(), "", end='')
    numbers.rotate(-matches[wanted]+1 if matches[wanted] > 0 else -matches[wanted])