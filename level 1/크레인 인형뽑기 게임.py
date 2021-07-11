def solution(board, moves): #14:31
    basket = []
    result = 0
    _board = []
    
    for i in range(len(board)): # board를 세로로 바꿈
        tmp = []
        for j in range(len(board)):
            tmp.append(board[j][i])
        _board.append(tmp)
     
    for i in moves:
        if sum(_board[i-1]) != 0: # 인형이 있을때만 뽑음
            p1 = _board[i-1].pop(0) # 인형 하나를 뽑음
            while p1 == 0: # 0이면 다음 걸로 넘어감.
                p1 = _board[i-1].pop(0) 
            if len(basket) == 0: # 바구니가 비었으면 인형 바로 추가
                basket.append(p1)
            else: # 바구니에 인형이 있다면
                p2 = basket[-1] # 제일 위에있는 인형을 뽑아서
                if p1 == p2: # 같다면 
                    result += 2 # 점수 +
                    basket.pop(-1) # 바구니에서 인형 제거
                else:  # 같지 않다면
                    basket.append(p1) #뽑은 인형 바구니에 추가
    return result
