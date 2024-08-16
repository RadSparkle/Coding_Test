while True:
    a = input()
    if a == '0':
        break
    if list(a) == list(reversed(a)):
        print('yes')
    else:
        print('no')