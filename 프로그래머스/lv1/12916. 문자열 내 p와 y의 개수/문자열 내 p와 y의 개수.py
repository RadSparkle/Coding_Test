def solution(s):
    s = s.upper()
    s = list(s)
    y_cnt = s.count('Y')
    p_cnt = s.count('P')
    if y_cnt == p_cnt :
        return True
    else : 
        return False