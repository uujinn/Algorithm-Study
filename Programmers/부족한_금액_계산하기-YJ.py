"""
price: 놀이기구의 이용료
money: 처음 가지고 있던 금액
count: 놀이기구의 이용 횟수
""" 

def solution(price, money, count):
    sum = 0
    for i in range(count):
        sum += (i + 1) * price
    
    return sum - money if sum - money > 0 else 0

print(solution(3, 100, 4))