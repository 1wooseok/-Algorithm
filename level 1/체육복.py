def solution(n, lost, reserve):
    _reserve = [i for i in reserve if i not in lost] # 여벌이 있는데 도난당한 학생을 제외하고 시작.
    _lost = [i for i in lost if i not in reserve]
    
    for i in _reserve: # 여벌이 있는 학생들 중
        if (i-1) in _lost: # 빌려줄 수 잇으면
            _lost.remove(i-1) # 빌려주고 삭제
        elif (i+1) in _lost: 
            _lost.remove(i+1) 
             
    return n - len(_lost) # 전체 - 마지막까지 못빌린 학생

# 무조건 한명씩 검사 해야함.