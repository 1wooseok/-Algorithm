def solution(s): # 16:24 - 16:43
    s = s+' '
    eng = {'zero': 0, 'one': 1, 'two' :2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven': 7, 'eight': 8, 'nine':9}
    answer = ''
    if s.isdigit():
        return int(s)
    else:
        tmp = ''
        for i in s:
            if tmp in eng:
                tmp = str(eng[tmp])
                answer = answer + tmp
                tmp = ''
            if i.isdigit():
                answer = answer + tmp + i
                tmp = ''
            else:
                tmp = tmp + i
                
    return int(answer)


# 
def solution(s):
    eng = {'zero': '0', 'one': '1', 'two' :'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven': '7', 'eight': '8', 'nine':'9'}
    for e in eng:
        s = s.replace(e, eng[e])
    return int(s)
    
