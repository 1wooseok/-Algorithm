def solution(nums):
    N = len(nums)/2
    _nums = list(set(nums))
    n = len(_nums)
    if n > N:
        return N
    return n
