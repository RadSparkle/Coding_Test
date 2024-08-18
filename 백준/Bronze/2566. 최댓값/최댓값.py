list_a = []

for _ in range(9):
    list_a.append(input().split())

sum = 0
answer = []
for i in range(9):
    for k in range(9):
        tmp = int(list_a[i][k])
        if sum < tmp or sum == tmp:
            sum = tmp
            answer = sum, i+1, k+1

print(answer[0])
print(answer[1], answer[2])