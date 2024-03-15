def longest_array_index(arr):
    lengths = [len(sub_arr) for sub_arr in arr]

    max_lengths = max(lengths)

    if lengths.count(max_lengths) > 1:
        return '?'

    max_index = lengths.index(max_lengths)
    return chr(max_index+65)

alphabet = input().upper()

alphabet_list = [[] for _ in range(26)]


for char in alphabet:
    alphabet_list[ord(char)-65].append(1)

print(longest_array_index(alphabet_list))