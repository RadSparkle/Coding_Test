result_list = [0] * 26
alphabet_list = list(input())

for i in alphabet_list:
    result_list[ord(i)-97]+=1

for i in result_list:
    print(i, end=' ')