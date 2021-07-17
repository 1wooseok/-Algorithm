def solution(numbers, hand): # 23 : 13
    # 2차원 리스트의 index를 좌표로 사용
    dial = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    
    # i 로부터 c, l 을 어떻게 얻을것인지
    dial[c][l]
    
    answer = ''
    left_hand_pos = None
    right_hand_pos = None
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left_hand_pos = i
        elif i in [3,6,9]:
            answer+= 'R'
            right_hand_pos = i
        else: # 가운데 라인 # 누르기전에 거리 계산 # 거리가 같다면, hand 체크.
            
    return answer
        
