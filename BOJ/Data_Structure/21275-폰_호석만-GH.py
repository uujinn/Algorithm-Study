import sys

input = sys.stdin.readline

A, B = input().split()
x, a, b = 0, 0, 0
count = 0


for i in range(2, 36 + 1):
    try:
        a_ = int(A, i)
    except:
        continue

    for j in range(2, 36 + 1):
        try:
            b_ = int(B, j)
            if a_ == b_ and i != j:
                count += 1
                x = a_
                a = i
                b = j
        except:
            continue

if count == 1:
    print(x, a, b)

elif count == 0:
    print("Impossible")
else:
    print("Multiple")