N = int(input())
tmp = 0
string_list = []
answer = []

for _ in range(N):
    string_list.append(input())

string_list_set = list(set(string_list))

for i in string_list_set:
    count = string_list.count(i)
    if tmp < count:
        answer.clear()
        answer.append(i)
    elif tmp > count:
        continue
    elif tmp == count:
        answer.append(i)
    tmp = count

answer.sort()
print(answer[0])