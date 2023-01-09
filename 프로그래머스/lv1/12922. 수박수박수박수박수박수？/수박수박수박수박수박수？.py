def solution(n):
    su_list = ["수","박"]
    result_list = []
    k=0
    for i in range(n):
        if k == 0 :
            k = 1
            result_list.append(su_list[0])
        elif k == 1 :
            k = 0
            result_list.append(su_list[1])
            
    return ''.join(result_list)