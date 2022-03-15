from sys import stdin
N = int(stdin.readline())
expression = str(stdin.readline().rstrip())
temp = []
temp_num = {}
for i in range(N):
    temp_num[chr(i + 65)] = str(stdin.readline().rstrip())

for e in expression:
    if e.isalpha():
        temp.append(temp_num[e])
    else:
        back = temp.pop()
        front = temp.pop()
        
        temp.append(eval(str(front) + e + str(back)))

print('%0.2f'%(temp[-1]))