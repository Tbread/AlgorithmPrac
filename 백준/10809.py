a = input()
alphabet_occurrence_array = [-1] * 26
i = -1
for char in a:
    i += 1
    m = ord(char) - ord('a')
    if alphabet_occurrence_array[m] == -1:
        alphabet_occurrence_array[m] = i


str = str(alphabet_occurrence_array)[1:-1]
str_rep = str.replace(',','')
print(str_rep)