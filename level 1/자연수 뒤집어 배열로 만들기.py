def solution(n):
    n = list(map(int, str(n)))
    a = len(n)//2
    for i in range(a):
        print(i)
        n[i] , n[-(i+1)] = n[-(i+1)], n[i]
    return n
