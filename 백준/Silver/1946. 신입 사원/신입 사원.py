import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank_sort = sorted(rank)
    result = 1
    top = 0

    for i in range(1, len(rank_sort)):
        if rank_sort[i][1] < rank_sort[top][1]:
            result+=1
            top = i
    print(result)