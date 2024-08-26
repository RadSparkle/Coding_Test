from collections import Counter

result = []
for _ in range(int(input())):
    result.append(input().split('.')[1])

word_dict = dict(sorted(Counter(result).items(), key=lambda item: item[0], reverse=False))

for i, k in word_dict.items():
    print(i, k)
