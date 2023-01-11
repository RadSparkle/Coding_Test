def solution(arr):
    result = []
    for i in range(1,len(arr)) :
        if arr[i-1] != arr[i] :
            result.append(arr[i-1])
        if i+1 == len(arr) :
            result.append(arr[-1])
    return result