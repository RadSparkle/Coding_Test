N = int(input())
people = []
result = []
for _ in range(N):
    people.append(list(map(int, input().split(' '))))

for i in people:
    rank = 1
    for a in people:
        if i[0] < a[0] and i[1] < a[1]:
            rank +=1
    print(rank, end =' ')