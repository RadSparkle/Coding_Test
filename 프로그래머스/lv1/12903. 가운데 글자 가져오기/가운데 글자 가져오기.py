import math

def solution(s):
    s_list = list(s)
    result = []
    if len(s) % 2 == 0 :
        a = s_list[int((len(s) / 2) -1)]
        b = s_list[int(len(s) / 2)]
        result.append(a)
        result.append(b)
    else :
        a = s_list[math.floor(len(s) / 2)]
        result.append(a)
    return ''.join(result)