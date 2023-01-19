import sys

n = int(sys.stdin.readline())
n_list = sorted(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

def solution(a) :
    left = 0
    right = len(n_list)-1

    while left <= right :
        mid = (left + right) // 2
        if n_list[mid] == a :
            return 1
        elif n_list[mid] > a :
            right = mid -1
        elif n_list[mid] < a :
            left = mid +1
    return 0


for i in m_list :
    print(solution(i))
