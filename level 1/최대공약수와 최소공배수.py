def solution(n, m):
    answer = []
    # 최대 공약수
    for i in range(m+1, 0, -1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break;
    
    # 최소 공배수
    for i in range(m, n*m+1):
        if i%n == 0 and i%m == 0:
            answer.append(i)
            break;
            
    return answer
