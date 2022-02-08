import sys
input = sys.stdin.readline

str = list(input().rstrip())[::-1]

def cal(first):
    re = 0
    while str:
        s = str.pop()
        
        if s == "(" or s == "[":
            re += cal(s)
            
        elif first == "(" and s == ")":
            return 2 * max(1, re)
        
        elif first == "[" and s == "]":
            return 3 * max(1, re)
    
    print(0)    # 리스트에 값이 없는데 return 안 되면 바보 괄호
    sys.exit()

answer = 0    

while str:
    answer += cal(str.pop())
print(answer)