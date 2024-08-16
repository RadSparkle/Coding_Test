N, M = map(int, input().split())

s = []
target = []
answer = 0

for _ in range(N):
    s.append(input())

for _ in range(M):
    target.append(input())

for i in target:
    if s.count(i) > 0:
        answer+=1
print(answer)