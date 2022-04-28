from sys import stdin

N = int(stdin.readline())
count, answer = 0, 0
temp = N

while N != answer:
    if temp < 10:
        hap = temp
    else:
        hap = temp // 10 + temp % 10

    answer = (temp % 10) * 10 + hap % 10
    temp = answer
    count += 1
    
print(count if count > 1 else 1)