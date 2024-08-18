
answer = []

for _ in range(int(input())):
    age, user = input().split()
    answer.append([int(age), user])

for i in sorted(answer, key=lambda x: x[0]):
    print(i[0], i[1])