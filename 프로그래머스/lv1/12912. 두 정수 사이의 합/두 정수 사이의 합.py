def solution(a, b):
    result = 0
    for i in range(a,b+1) :
        result += i
    if result == 0 :
        for i in range(b,a+1) :
            result+=i
    return result