n = int(input())

a = list(map(int, input().split()))
new_list = list()

max_score = max(a)

for i in a:
    new_list.append((i/max_score)*100)
print(sum(new_list)/len(new_list))