from sys import stdin

dict = {}
answer = ''

N, M = map(int, stdin.readline().split())

for i in range(N):
    dict[i + 1] = stdin.readline().rstrip()
reverse_dict = {v : k for k, v in dict.items()}

for i in range(M):
    temp = stdin.readline().rstrip()
    
    if temp.isdigit():
        print(dict.get(int(temp)))
        
    elif temp.isalpha():
        print(reverse_dict.get(temp))
        
# 284ms