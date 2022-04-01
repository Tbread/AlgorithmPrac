a = input()
alphabet_occurrence_array = [0] * 26
a = a.lower()
for char in a:
    m = ord(char) - ord('a')
    alphabet_occurrence_array[m] += 1

b = list(reversed(sorted(alphabet_occurrence_array)))

if b[0] == b[1]:
    print('?')
else:
    x = alphabet_occurrence_array.index(b[0])
    m = ord('a')+x
    set = chr(m)
    set = set.upper()
    print(set)
