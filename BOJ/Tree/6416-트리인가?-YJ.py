from sys import stdin

# 인풋을 전부 다 받고 시행
all_input = []
while True:
    try:
        # 줄마다 끊어서 input
        tmp = list(map(int, stdin.readline().rstrip().split()))
        # print(tmp)
        if tmp == [-1, -1]:
            break
        all_input.append(tmp)
    except:
        break

# print(all_input)

cases = []  # case1, 2, 3
case_part = []  # ex. case1 - (6, 8) (5, 3) (5, 2) (6, 4) // (5, 6)

for line in all_input:  # 한 줄 마다 check
    # 줄 마지막이 [0, 0]이면 case_part에 그 앞 (u, v) 넣어주고 다음 case로 넘어감
    if line[-2:] == [0, 0]:
        case_part += line[:-2]
        cases.append(case_part)
        case_part = []
    else:  # 아니라면 전체 다 case_part에 추가
        case_part += line


# print(cases)

for case in range(len(cases)):
    edges = cases[case]
    print(edges)

    # 트리 생성
    parent = dict()
    child = dict()
    vertex = set()

    for i in range(len(edges) // 2):
        # (6, 8) (5, 3) (5, 2) (6, 4), (5, 6)
        u, v = edges[i * 2], edges[i * 2 + 1]  # 여기서 (u, v) 뽑음
        print(u, v)
