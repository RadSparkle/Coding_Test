

N = int(input())
word_list = []
for _ in range(N):
    word_list.append(input())

word_lists = list(set(word_list))
word_lists.sort(reverse=False)
answer = word_lists
answer.sort(key=len)

for i in answer:
    print(i)