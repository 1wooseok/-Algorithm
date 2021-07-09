def solution(answer):
    score = [0,0,0]
    result =[]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    n = len(answer)
    
    for i in range(n): # 채점
        if answer[i] == a[i%len(a)]:
            score[0] += 1
        if answer[i] == b[i%len(b)]:
            score[1] += 1
        if answer[i] == c[i%len(c)]:
            score[2] += 1 
            
    max = score[0]
    for i in range(1,len(score)): # 최대값
        if score[i] > max:
            max = score[i]
    
    for i in range(len(score)): # 1등 or 공동1등
        if score[i] == max:
            result.append(i+1)
            
    return result
