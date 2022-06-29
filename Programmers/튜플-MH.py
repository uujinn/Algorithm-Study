import re

def solution(_s):
    s = list(map(str, _s.split(',{')))
    # ['{{4,2,3}', '3}', '2,3,4,1}', '2,3}}']

    tuples = []
    pattern = re.compile('\d+')
    for tuple in s:
        temp = pattern.findall(tuple)
        tuples.append(temp)
    # tuples : [['4', '2', '3'], ['3'], ['2', '3', '4', '1'], ['2', '3']]
    
    answer = []
    tuples.sort(key = len)
    # tuples : [['3'], ['2', '3'], ['4', '2', '3'], ['2', '3', '4', '1']]
    
    for tuple in tuples:
        temp = [t for t in tuple if t not in answer]
        answer.extend(temp)   
    
    return [int(a) for a in answer]

print(solution(	"{{4,2,3},{3},{2,3,4,1},{2,3}}"))