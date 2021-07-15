def solution(skill, skill_trees):
    myskill = list(skill)
    result = 0
    
    for i in skill_trees:
        mytree = []
        flag = True
        for j in i:
            if j in myskill:
                mytree.append(j)
        for k in range(len(mytree)):
            if mytree[k] != myskill[k]:
                flag = False
        if flag:
            result += 1
    return result
