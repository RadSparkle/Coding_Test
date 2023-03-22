import sys

n = int(sys.stdin.readline().rstrip('\n'))
m = int(sys.stdin.readline().rstrip('\n'))
n_list = list(map(int,sys.stdin.readline().split()))

n_list.sort()
start=0
end=n-1
cnt=0
while start<end:
    if n_list[start] + n_list[end] == m:
        start+=1
        end-=1
        cnt+=1
    if n_list[start] + n_list[end] < m:
        start+=1
    if n_list[start] + n_list[end] > m:
        end-=1
print(cnt)