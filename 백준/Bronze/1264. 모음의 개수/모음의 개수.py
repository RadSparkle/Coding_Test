collection = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while(True):
    count=0
    eng_sentence = input()
    if eng_sentence=='#':
        break
    
    for s in eng_sentence:
        if s in collection:
            count+=1
    print(count)