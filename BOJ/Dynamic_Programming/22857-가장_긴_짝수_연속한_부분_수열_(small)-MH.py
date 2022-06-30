from sys import stdin

N, K = map(int, stdin.readline().split())
S = list(map(int, stdin.readline().split()))

pattern = []
temp = 0
prev = True     # i - 1번째 숫자가 짝수면 True

for i in range(len(S)):
    if S[i] % 2 == 0:
        if not prev:                    # 이전 숫자가 짝수가 아니면
            pattern.append(temp)
            temp = 0
        temp += 1
        prev = True
        
    else:
        if prev and i != 0:             # 이전 숫자가 홀수가 아니면
            print('*')
            pattern.append(temp)
            temp = 0
        temp -= 1   
        prev = False
        
pattern.append(temp)
print(pattern)
# pattern : [-1, 1, -1, 1, -1, 1, -1, 1]