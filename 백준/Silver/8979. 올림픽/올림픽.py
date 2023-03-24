n, k = map(int,input().split())
score = []

for i in range(n):
    a= input().replace(' ','')
    score.append(a)
    if i==k-1:
        target=a

score.sort(reverse=True)
print(score.index(target)+1)
