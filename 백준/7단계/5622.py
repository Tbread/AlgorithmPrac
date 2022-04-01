a = input().lower()
i = 0
for char in a:
    m = ord(char) - ord('a')
    if m < 3:
        i += 3
    elif m < 6:
        i += 4
    elif m < 9:
        i += 5
    elif m < 12:
        i += 6
    elif m < 15:
        i += 7
    elif m < 19:
        i += 8
    elif m < 22:
        i += 9
    elif m < 26:
        i += 10
print(i)
