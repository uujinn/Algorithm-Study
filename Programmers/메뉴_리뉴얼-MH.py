from itertools import combinations

def is_same(comb, num):
    
    return


def solution(orders, course):
    answer = []    
    arr = [[] for _ in range(len(course))]
    
    for i in range(len(course)):            # 2, 3, 4
        for order in orders:
            for comb in combinations(order, course[i]):
                if comb not in arr[i]:
                    arr[i].append(comb)
    print(arr)
    
    for i in range(len(arr)):
        for comb in arr[i]:
            flag = True
            
            for order in orders:
                print(set(comb))
                print()
                print(set(order))
                print(set(comb))
                print(set(comb) & set(order))

                if set(comb) & set(order) != set(comb):
                    print('bad')
                    flag = False
                    break
                else:
                    print('good')
                print('***')
                
            if flag:
                answer.append(comb)
        print('-------------')
                
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]))