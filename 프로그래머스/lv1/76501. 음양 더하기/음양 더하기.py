def solution(absolutes, signs):
    signs_list = []
    for i in signs :
        if i == True :
            signs_list.append(1)
        else :
            signs_list.append(-1)
    
    result = [absolutes[i] * signs_list[i] for i in range(len(absolutes))]
    
    return sum(result)