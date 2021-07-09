# 에라토스테네스의 채

def solution(n):
    primes = 0
    li = [False, False] + [True]*(n-1) # True -> 소수
    
    for i in range(2, n+1): 
        if li[i]: # 소수이면 
            primes += 1 # + 1
            for j in range(2*i, n+1, i): # i의 배수는 더이상 소수가 아님.
                li[j] = False
    return primes
