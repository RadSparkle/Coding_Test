def solution(n):
    result = 0
    i = 0
    while i <= n :
        if pow(i,2) == n :
            return pow(i+1,2)
        i += 1
    if result == 0 :
        return -1