T = int(input())
answer = []

while T > 0:
    a, b = input().split()
    string_list = [i for i in b]
    tmp = []
    for i in string_list:
        tmp.append(i*int(a))
    answer.append(tmp)
    T-=1

for i in answer:
    print(''.join(i))
