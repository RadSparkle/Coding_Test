from itertools import combinations

def solution(numbers):
    test = list(combinations(numbers,2))
    answer = []
    for i in test :
        answer.append(sum(i))
    answer = list(set(answer))
    answer.sort()
    return list(answer)