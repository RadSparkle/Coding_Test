N, M, K = map(int, input().split())

answer = 0

sit = []

for _ in range(N):
    start = 0
    end = K
    sit = [int(i) for i in input()]

    while end <= M:
        if sum(sit[start:end]) > 0:
            start+=1
            end+=1
        else:
            answer+=1
            start+=1
            end+=1
print(answer)