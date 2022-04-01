import sys
def get_star(n):
    if n == 1:
        return ['*']

    stars = get_star(n//3)
    arr = []
    for star in stars:
        arr.append(star*3)
    for star in stars:
        arr.append(star+' '*(n//3)+star)
    for star in stars:
        arr.append(star*3)
    return arr

n = int(sys.stdin.readline())
print('\n'.join(get_star(n)))