t = int(input())
r = 0
for i in range(t):
    n = 0
    a = input()
    alphabet_occurrence_array = [0] * 26
    for char in a:
        m = ord(char) - ord('a')
        alphabet_occurrence_array[m] += 1


    for i in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[i] > 1:
            m = ord('a') + i
            str = chr(m) * alphabet_occurrence_array[i]
            if a.find(str) == -1:
                n += 1
    if n == 0:
        r += 1
print(r)