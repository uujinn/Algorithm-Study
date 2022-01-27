from sys import stdin

num_list = []
stack = []
n = int(stdin.readline())
postfix = stdin.readline().rstrip()

for i in range(n):
    num_list.append(stdin.readline().rstrip())

for idx, char in enumerate(postfix):                    # 숫자면 push 기호면 계산
    if char.isalpha():
        stack.append(num_list[ord(char) - ord('A')])
    else:     
        stack.append(str(eval(stack.pop(-2) + char + stack.pop(-1))))
        
print("{0:.2f}".format(float(stack[0])))