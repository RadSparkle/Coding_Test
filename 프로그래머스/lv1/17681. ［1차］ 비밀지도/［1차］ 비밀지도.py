def solution(n, arr1, arr2):
    arr1_list = []
    arr2_list = []
    result = []

    res = []
    for i in arr1 :
        arr1_list.append(int(format(i,'b')))
    for i in arr2 :
        arr2_list.append(int(format(i,'b')))
    for i in range(len(arr1_list)) :
        result.append(list(str(arr1_list[i] + arr2_list[i]).zfill(n)))
    for i in result :
        answer = ''
        for k in range(len(result)) :
            i[k] = int(i[k])
            if i[k] >= 1 :
                answer += '#'
            else :
                answer += ' '
        res.append(answer)
    return res





