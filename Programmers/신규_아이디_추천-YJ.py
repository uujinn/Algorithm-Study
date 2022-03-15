import re

def solution(new_id):

    # 정규식 사용
    new_id = re.sub('[^a-z\d_.\-]', '', new_id.lower()) # 1,2단계
    new_id = re.sub('[.]+','.', new_id) # 3단계
    new_id = re.sub('^[.]|[.]$', '', new_id) # 4단계
    new_id = "a" if len(new_id) == 0 else new_id # 5단계
    new_id = new_id[:15] if len(new_id) >= 16 else new_id # 6단계
    new_id = re.sub('[.]$', '', new_id) 

    while len(new_id) < 3: # 7단계
        new_id = new_id + new_id[-1]
    
    return new_id


print(solution("z-+.^."))
