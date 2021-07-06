def solution(n, arr1, arr2):
    _arr1 = []
    _arr2 = []
    result = []
    answer = []
    
    for i in arr1: # arr1 이진수 변환
        tmp = []
        while i >= 1:
            if i <= 1:
                tmp.insert(0, i)
                break;
            r = i%2
            tmp.insert(0, r)
            i = i//2
        _arr1.append(tmp)
    
    for i in arr2: # arr2 이진수 변환
        tmp = []
        while i >= 1:
            if i <= 1:
                tmp.insert(0, i)
                break;
            r = i%2
            tmp.insert(0, r)
            i = i//2
        _arr2.append(tmp)
    
    for i in _arr1: # arr1 0채워넣기
        while len(i) < n:
            i.insert(0, 0)
        
    for i in _arr2: # arr2 0채워넣기
        while len(i) < n:
            i.insert(0, 0)  
            
    for i in range(n): # '#', ' ' 포맷으로 변환
        tmp = []
        for k in range(n):
            if _arr1[i][k]+_arr2[i][k] > 0:
                tmp.append('#')
            else:
                tmp.append(' ')
        result.append(tmp)
        
    
    for i in result: # str으로 변환
        s = ''.join(i)
        answer.append(s)
    return answer





# 비트 연산
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = str(bin(arr1[i] | arr2[i]))[2:]
        tmp=tmp.rjust(n,'0')
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0',' ')
        answer.append(tmp)
    return answer
