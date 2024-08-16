string_list = [i for i in input()]
answer = [-1 for i in range(26)]

for idx, val in enumerate(string_list):
    if answer[ord(val)-97] == -1:
        answer[ord(val)-97] = idx

for i in answer:
    print(i, end=' ')