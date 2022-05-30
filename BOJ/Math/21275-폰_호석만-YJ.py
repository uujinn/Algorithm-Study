X_A, X_B = input().split()

X, A_i, B_j = 0, 0, 0
cnt = 0

for i in range(2, 37):
    try:
        A_ten = int(X_A, i)  # X_A가 i 진수라고 가정하고 십진법 A로 변환
    except:  # 못바꾸는 경우
        continue
    if cnt > 1:
        print('Multiple')
        exit(0)
    for j in range(2, 37):
        try:
            B_ten = int(X_B, j)
        except:
            continue

        if A_ten == B_ten and i != j:
            X = A_ten
            A_i = i  # i진수
            B_j = j  # j진수
            cnt += 1
            if cnt > 1:  # Multiple
                break

if cnt == 0:
    print('Impossible')
else:
    print(f'{X} {A_i} {B_j}')
