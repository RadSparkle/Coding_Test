def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        cnt = 0
        for k in range(1, i + 1):
            if i % k == 0:
                cnt += 1
        if cnt % 2 == 0:
            result += i
        elif cnt %2 != 0 :
            result -= i
    return result
            
        