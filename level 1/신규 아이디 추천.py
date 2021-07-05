def solution(new_id):
    # 1
    new_id = new_id.lower() 
    
    # 2
    spcl = ['-', '_', '.']
    for i in new_id: 
        if not i.isalpha() and not i.isdigit():        
            if i not in spcl:
                new_id = new_id.replace(i, '')
    
    # 3
    s = ''
    cnt = 0
    for i in new_id:
        if i == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt <= 1:
            s += i
    new_id = s
    
    
    # 4
    if new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0:
        if new_id[-1] == '.': 
            new_id = new_id[:-1]

    # 5
    new_id = new_id.replace(' ', 'a', 15) 
    
    # 6
    if len(new_id) > 15: 
        new_id = new_id[:15]
    if len(new_id) == 0:
        new_id = 'aaa'
    else:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7  
    while len(new_id) < 3:
        new_id += new_id[-1]
        
    # return
    return new_id
