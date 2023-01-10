def solution(s):
    s_list = list(s)
    alphabet_list = []
    for i in s_list:
        alphabet_list.append(ord(i))
    alphabet_list.sort(reverse=True)

    s_list = []
    for k in alphabet_list:
        s_list.append(chr(k))
    return ''.join(s_list)