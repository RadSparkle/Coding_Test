def solution(t,p) :
    len_list = []
    t = list(t)
    b = 0
    m = len(p)
    answer = 0
    for i in range(len(t)) :
        k = t[b:m]
        f = ''.join(k)
        if f <= p :
            answer+=1
        b+=1
        m+=1
        if m == len(t)+1 :
            break
    return answer
solution('500220839878','7')