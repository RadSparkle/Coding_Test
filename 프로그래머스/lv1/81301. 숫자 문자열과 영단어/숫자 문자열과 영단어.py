def solution(s):
    eng_list = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for i in range(10):
        k = eng_list[i]
        if k in s:
            s = s.replace(k,str(i))
    return int(s)