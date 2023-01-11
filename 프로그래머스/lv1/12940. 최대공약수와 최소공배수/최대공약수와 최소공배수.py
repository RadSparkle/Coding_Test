def solution(n, m):
    l = n*m
    while n!=0 :
        r = m % n
        m = n
        n = r

    k = l //m
    return [m,k]