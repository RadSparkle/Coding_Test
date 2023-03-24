n = list(1 for _ in range(int(input())))
s = int(input())
answer= []

for _ in range(s):
    a, b = map(int,input().split())
    b-=1
    for k in range(a-1, b):
        if k == b:
            n[k]=1
        elif k != b:
            n[k]=0
print(sum(n))

