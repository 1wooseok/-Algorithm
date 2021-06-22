def solution(array, commands):
    n = len(commands)
    answer = []
    for i in range(n):
        start = commands[i][0]-1
        end = commands[i][1]
        
        new_array =  array[start:end]
        new_array.sort()

        k = commands[i][2]-1
        if k >= len(new_array):
            k = -1

        answer.append(new_array[k])
    return answer
