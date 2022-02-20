# 약수 개수 구하기
def getDivisor(x):
    num = 0
    for i in range(1, int(x/2) + 1): 
        if x % i == 0:
            num += 1
    return num + 1 # 자기 자신 더해줌

# 짝수 판별
def isEven(x):
    if x % 2 == 0:  return True
    else:   return False

def solution(left, right):
    sum = 0
    for i in range(left, right + 1):
        x = getDivisor(i)
        if isEven(x):
            sum += i
        else: sum -= i
    return sum
