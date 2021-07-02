def solution(n):
    r_tri = [] # 3진수를 거꾸로 담을 배열
    result = 0
    while True: # 10진수 -> 3진수 변환 
        if n < 3:  # 몫이 3보다 작은 경우
            r_tri.append(n)  # 몫을 배열 맨뒤에 추가
            break # 더이상 나누지 않음.  
        r_tri.append(n%3) # 3으로 나눈 나머지 배열뒤에 추가 ( 항상 제일 뒤에 추가하기 때문에 3진수가 거꾸로 됨) 
        n = n//3
       
    x = len(r_tri)-1
    for i in range(x, -1, -1): # 뒤에서부터 0까지
        result += r_tri[i] * (3**(x-i)) # 배열 값 * 3의 n승 ( n = 0, 1, 2, 3 ,,, )
    return result