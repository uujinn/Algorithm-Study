import re

def solution(new_id):

    new_id = new_id.lower() # 1단계
    
    # 정규식 사용
    new_id = re.sub('[^a-z\d\-_.]', '', new_id) # 2단계
    new_id = re.sub('\.+','.', new_id) # 3단계

    
    if new_id[0] == '.': # 4단계
        new_id = new_id[1:]
        if len(new_id) != 0 and new_id[-1] == '.':
            new_id = new_id[:-1]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]
    

    if len(new_id) == 0: # 5단계
        new_id = 'a'
    elif len(new_id) >= 16: # 6단계
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]
    

    if len(new_id) <= 2: # 7단계
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
