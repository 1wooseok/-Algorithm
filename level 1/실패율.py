def solution(N, stages):
    fail = []
    answer = []
    
    # 실패율 계산
    for stage in range(1, N+1): 
        reach = 0 # 도달한 user 
        stay = 0 # 머물러있는 user
        for user in stages:
            if user >= stage: # 도달
                reach += 1 
            if user == stage: # 머물러 있는 경우
                stay += 1
        if reach == 0: # reach가 0일 경우 에러
            fail.append((0, stage))
        else:
            fail.append((stay/reach, stage))
                    
    # 정렬        
    result = sorted(fail, key = lambda x : x[0], reverse=True)
    
    for i in result:
        answer.append(i[1])
        
    return answer
