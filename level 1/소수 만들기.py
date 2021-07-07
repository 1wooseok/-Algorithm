def solution(nums):
    _nums = []
    answer = 0
    for i in range(len(nums)-2): # 서로다른 숫자 3개 조합
        for k in range(i+1, len(nums)-1):
            for j in range(k+1, len(nums)):
                _nums.append(nums[i]+nums[j]+nums[k])
    #_nums = list(set(_nums))
    
    for i in _nums: # 소수 판별식
        cnt = 0
        for k in range(2, i+1):
            if i%k == 0:
                cnt += 1
            if cnt > 1:
                break;
        if cnt == 1: 
            answer += 1
    return answer
