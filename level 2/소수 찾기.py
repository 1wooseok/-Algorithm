def solution(numbers):
    cnt = 0 
    # 리스트로 변환
    li = [ i for i in numbers ]
    print(li)
    # 모든 경우의 수 조합
    comb = []
    
    
    # 소수 판별 ( 에라토스테네스의 채 )
    prime = [False, False] + ([ True ] * (max(comb)+1))
    for i in comb:
        if prime[i]:
            cnt += 1
            for k in range(2*i, prime[-1], i):
                prime[k] = False
    return cnt
