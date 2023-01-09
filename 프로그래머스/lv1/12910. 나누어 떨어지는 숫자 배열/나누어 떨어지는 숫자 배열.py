def solution(arr, divisor):
    result = []
    for i in arr :
        if i % divisor == 0 :
            result.append(i)
    result.sort(reverse=False)
    
    if len(result) > 0 :
        return result
    else :
        result.append(-1)
        return result