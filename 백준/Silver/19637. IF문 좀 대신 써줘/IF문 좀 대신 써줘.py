import sys
input = sys.stdin.readline
n, m = map(int,input().split())
s = []
for _ in range(n):
    a, b =map(str, input().split())
    s.append([a,int(b)])

s.sort(key=lambda x:x[1])
for _ in range(m):
    q = int(input())
    start = 0
    end = len(s) - 1
    while start <= end:
        mid = (start + end) // 2
        if s[mid][1] < q:
            start = mid + 1
        else:
            end = mid - 1
    print(s[start][0])