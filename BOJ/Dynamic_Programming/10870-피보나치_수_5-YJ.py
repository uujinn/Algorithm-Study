n = int(input())

n_1 = 0
n_2 = 0
value = 0

for i in range(n+1):
    if i == 0:
        n_1 = 0
    elif i == 1:
        value = 1
        n_2 = 1
    else:
        n_2 = n_1
        n_1 = value
        value = n_1 + n_2

print(value)
