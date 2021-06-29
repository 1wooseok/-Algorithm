def solution(s):
    answer = ""
    n = len(s)
    cnt = 0
    for i in range(n):
        if s[i] == ' ':
            cnt = -1
        if cnt%2 == 0:
            ch = s[i].upper()
        else:
            ch = s[i].lower()
        answer += ch 
        cnt += 1
    return answer
