def solution(n, arr1, arr2):
    _arr1 = []
    _arr2 = []
    result = []
    
    for i in arr1:
        tmp = []
        while i >= 1:
            if i <= 1:
                tmp.insert(0, i)
                break;
            r = i%2
            tmp.insert(0, r)
            i = i//2
        _arr1.append(tmp)
    
    for i in arr2:
        tmp = []
        while i >= 1:
            if i <= 1:
                tmp.insert(0, i)
                break;
            r = i%2
            tmp.insert(0, r)
            i = i//2
        _arr2.append(tmp)
    
    for i in _arr1:
        while len(i) < n:
            i.insert(0, 0)
        
    for i in _arr2:
        while len(i) < n:
            i.insert(0, 0)  
            
    for i in range(n):
        tmp = []
        for k in range(n):
            if _arr1[i][k]+_arr2[i][k] > 0:
                tmp.append('#')
            else:
                tmp.append(' ')
        result.append(tmp)
        
    b = []
    for i in result:
        a = ''.join(i)
        b.append(a)
    return b





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
