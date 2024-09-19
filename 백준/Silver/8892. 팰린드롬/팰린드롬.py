from collections import deque
import itertools

def palindrome(str):
    while len(str) > 1:
        if str.popleft() != str.pop():
            return False
    return True

t = int(input())

for _ in range(t):
    k = int(input())
    str_list = []
    palindrome_list = []
    for _ in range(k):
        str_list.append(input())

    q = itertools.permutations(str_list, 2)
    for i in q:
        a = ''.join(i)
        b = deque(a)
        if palindrome(b):
            palindrome_list.append(a)

    if len(palindrome_list) > 0:
        print(palindrome_list.pop())
    else:
        print(0)
