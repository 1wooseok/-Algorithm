def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    my_lottos = [ i for i in lottos if i != 0] # 0제외하고 시작
    zero_num = len(lottos) - len(my_lottos) # 0의 개수
    min = 0
    
    for i in my_lottos:
        if i in win_nums: 
            win_nums.remove(i)
            min += 1

    return [rank[min + zero_num] , rank[min]]
