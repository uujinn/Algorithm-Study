from collections import Counter

def get_set(str):
    set = []
    
    for i in range(len(str) - 1):
        temp = str[i : i + 2]
        if temp.isalpha():
            set.append(temp) 
    return set    


def solution(str1, str2):
    answer = 0
    set1, set2 = get_set(str1.lower()), get_set(str2.lower())

    intersection = Counter(set1) & Counter(set2)                                  # 교집합
    union = list((Counter(set1) + Counter(set2) - intersection).elements())       # 합집합
    intersection = list(intersection.elements())
    
    try:
        answer = len(intersection) / len(union)
    except:
        answer = 1
        
    return int(answer * 65536)

print(solution("FRANCE", "french"))