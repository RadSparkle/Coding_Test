import math

def solution(arr):
    num_min = min(arr)
    arr.remove(num_min)
    if len(arr) == 0 :
        arr.append(-1)
    return arr