import sys
from collections import deque

def stack_sequence():
    stack = deque()
    stack_start = 1         # stack에 몇 번째 숫자까지 담겼는지 확인
    str = ''
    
    input_numbers = []
    for i in range(int(sys.stdin.readline())):
        input_numbers.append(int(sys.stdin.readline()))

    for num in input_numbers:      
        if num >= stack_start:
            for i in range(stack_start, num + 1):
                stack.append(i)
                stack_start += 1
                str += '+\n'    
        elif stack and num != stack[-1]:
            print('NO')
            return
        
        stack.pop()
        str += '-\n'
         
    print(str.rstrip())
    
stack_sequence()