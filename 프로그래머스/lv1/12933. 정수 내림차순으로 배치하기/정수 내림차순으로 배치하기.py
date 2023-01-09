def solution(n):
    n_list = list(map(int,str(n)))
    n_list.sort(reverse=True)
    result = int("".join(map(str,n_list)))
    return result