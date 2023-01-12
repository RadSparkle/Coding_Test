def solution(d, budget):
    d.sort(reverse=False)
    cnt = 0
    k = 0
    for i in d :
        k+=i
        if k > budget :
            break
        cnt +=1
    return cnt