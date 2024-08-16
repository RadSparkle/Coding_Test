import sys
import collections
N, M = map(int, input().split())
word_dict = {}
word_list = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        word_list.append(word)

words_count = collections.Counter(word_list)

for k, v in sorted(list(words_count.items())):
    word_dict[k] = v

sorted_dict = dict(sorted(word_dict.items(), key=lambda item: len(item[0]), reverse=True))
sorted_dict = dict(sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True))

for k, v in list(sorted_dict.items()):
    print(k)