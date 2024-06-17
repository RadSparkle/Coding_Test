playerCnt = int(input())
name_list = []
result = []
name_list_set = {}
for i in range(playerCnt):
    name_list.append(input()[:1])

name_list_set = set(name_list)

for i in name_list_set:
    if name_list.count(i) >= 5:
        result.append(i)

if not result:
    print('PREDAJA')
else:
    result.sort(reverse=False)
    print("".join(result))