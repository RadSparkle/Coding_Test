def solution(s):
    splitedStr = s.split(' ')
    result_list = []
    answer=[]
    real=''
    for i in splitedStr :
        result_list.append(int(i))
    result_list.sort(reverse=False)
    answer.append(str(result_list[0]))
    answer.append(str(result_list[-1]))
    real=' '.join(answer)
    return real