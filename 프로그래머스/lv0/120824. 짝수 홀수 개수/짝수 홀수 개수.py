
2
3
4
5
6
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer