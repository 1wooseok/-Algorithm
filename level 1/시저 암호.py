def solution(s, n):
    answer = "" # 정답을 담을 공백 문자열
    for i in s:
        ch = ord(i)
        if ch == 32: # 공백은 아무리 밀어도 공백
            ch = 32
            
        elif 90 < (ch+n) and ch < 91: # 대문자 ascii code 값을 넘을 경우
            ch = (ch+n)%90 + 64
        elif 96 < ch and 122 < (ch+n): # 소문자 ascii code 값을 넘을 경우
            ch = (ch+n)%122 + 96
        else: # 일반적인 경우
            ch = (ch+n)
        answer += chr(ch)
    return answer