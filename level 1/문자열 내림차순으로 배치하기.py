def solution(s):
    s = list(s)
    n = len(s)
    for i in range(1,n):
        key = s[i]
        j = i-1
        while j >=0 and key > s[j]:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = key
    return ''.join(s)        

s = "Zbcdefg"
solution(s)