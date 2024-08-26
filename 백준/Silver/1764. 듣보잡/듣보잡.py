n, m = map(int, input().split())

left = {}
right = []

for _ in range(n):
    word = input()
    left[word] = word

for _ in range(m):
    word = input()
    if word in left:
        right.append(word)

right.sort()
print(len(right))
for i in right:
    print(i)