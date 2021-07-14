def solution(a, b):
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    if a == 10:
        return day[(b+5)%7]
    elif a == 1 or a ==4 or a ==7:
        return day[(b+4)%7]
    elif a == 9 or a == 12: 
        return day[(b+3)%7]
    elif a == 6:
        return day[(b+2)%7]
    elif a == 3 or a == 11:
        return day[(b+1)%7]
    elif a ==2 or a == 8:
        return day[b%7]
    elif a == 5:
        return day[(b-1)%7]
