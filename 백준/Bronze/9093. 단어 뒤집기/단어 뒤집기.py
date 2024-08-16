T = int(input())

for _ in range(T):
    string = list(map(str, input().split(' ')))

    answer = []
    for i in string:
        answer.append(i[::-1])

    for i in answer:
        print(i, end = ' ')