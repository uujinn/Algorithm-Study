def solution(answers):
    
    answer = []

    babo_1 = [1,2,3,4,5]
    babo_2 = [2,1,2,3,2,4,2,5]
    babo_3 = [3,3,1,1,2,2,4,4,5,5]
    
    b1_score = 0
    b2_score = 0
    b3_score = 0
    
    for num in range(len(answers)):
        if answers[num] == babo_1[num%5]:
            b1_score += 1
        if answers[num] == babo_2[num%8]:
            b2_score += 1
        if answers[num] == babo_3[num%10]:
            b3_score += 1
            
    sol = [b1_score, b2_score, b3_score]

    for person, score in enumerate(sol):
        if score == max(sol):
            answer.append(person+1)
            
    return answer