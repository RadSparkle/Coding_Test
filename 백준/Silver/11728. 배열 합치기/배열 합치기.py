N, M = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.extend(b_list)
a_list.sort()

for i in a_list:
    print(i, end=' ')