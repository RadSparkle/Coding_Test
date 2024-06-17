word_list = list(map(str, input()))

reverse_word_list = []

for i in reversed(word_list):
    reverse_word_list.append(i)

while(len(word_list)!=0):
    a = word_list.pop()
    b = reverse_word_list.pop()
    if a != b:
        print(0)
        break
    elif len(word_list)==0:
        print(1)
        break