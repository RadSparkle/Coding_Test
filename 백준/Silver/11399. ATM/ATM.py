N = int(input())
P = list(map(int,input().split()))
P.sort(reverse=False)
answer = 0
for i in range(1,len(P)+1) :
    answer += sum(P[0:i])
print(answer)
