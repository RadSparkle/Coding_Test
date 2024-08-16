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

word_list = sorted(words_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in word_list:
    print(i[0])