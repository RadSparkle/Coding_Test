def solution(arr1, arr2):
    result = []
    answer = []
    for i in range(len(arr1)) :
        for k in range(len(arr1[0])) :
            answer.append(arr1[i][k]+arr2[i][k])
        result.append(answer)
        answer =[]
    return result
