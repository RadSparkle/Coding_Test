data = int(input())
list = list(map(int, input().split()))
target = int(input())

list.sort()

sum = 0
count = 0
right = data-1
left = 0

while left != right:
    if list[left] + list[right] == target:
        count+=1
        right -=1
    elif list[left] + list[right] > target:
        right -=1
    elif list[left] + list[right] < target:
        left += 1
print(count)