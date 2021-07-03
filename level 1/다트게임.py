def solution(dartResult): 
    dart = []
    s = ''
    for i in range(len(dartResult)): # 먼저 문자와 숫자 분리
        if dartResult[i].isnumeric():
            s += dartResult[i]
        else:
            if s != '':
                dart.append(s)
            dart.append(dartResult[i])
            s = ''

    s = [0, 0, 0]
    cnt = -1 # 몇번째 다트인지 
    for k in dart:
        if k.isnumeric(): # 반복하다가 숫자가 나오면 
            cnt += 1 # 다트를 던짐
            s[cnt] = int(k) # 점수 저장
        else:
            if k == 'D': # 제곱
                s[cnt] = s[cnt] * s[cnt]
            elif k == 'T': # 세제곱
                s[cnt] = s[cnt] * s[cnt] * s[cnt]
            elif k =='*': # 스타상
                s[cnt] = 2*s[cnt]
                if cnt != 0:
                    s[cnt-1] = 2*s[cnt-1]                
            elif k =='#': # 아차상
                s[cnt] = -s[cnt]
    return sum(s)
