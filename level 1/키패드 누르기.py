def solution(numbers, hand): # 23 : 13
    # index를 좌표로 사용
    coord = [(1,0), # 0
             (0,3), (1,3), (2,3), # 1 2 3
             (0,2), (1,2), (2,2), # 4 5 6
             (0,1), (1,1), (2,1), # 7 8 9
             (0,0), (2,0)  # '*', '#'
            ]
    
    answer = ''
    left_hand_pos = 10
    right_hand_pos = 11
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left_hand_pos = i
        elif i in [3,6,9]:
            answer += 'R'
            right_hand_pos = i
        elif i in [2,5,8,0]: # 가운데 라인. # 누르기전에 거리 계산.  # 거리가 같다면, hand 체크.
            l_dist = abs(coord[left_hand_pos][0] - coord[i][0]) + abs(coord[left_hand_pos][1] - coord[i][1])
            r_dist = abs(coord[right_hand_pos][0] - coord[i][0]) + abs(coord[right_hand_pos][1] - coord[i][1])
            if l_dist < r_dist:
                answer += 'L'
                left_hand_pos = i
            elif l_dist > r_dist:
                answer+= 'R'
                right_hand_pos = i
            elif l_dist == r_dist:
                if hand == 'left':
                    answer += 'L'
                    left_hand_pos = i
                else:
                    answer+= 'R'
                    right_hand_pos = i
    return answer
