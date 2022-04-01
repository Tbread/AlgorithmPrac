import sys
import itertools

comb = itertools.combinations
n = int(sys.stdin.readline().strip())
arr = []
ranked_arr = []
bulk_dict = {}
for i in range(n):
    inp = sys.stdin.readline().strip().split(' ')
    arr.append([int(inp[0]), int(inp[1]), i])
    bulk_dict[i] = 0
bulks = list(comb(arr, 2))
for bulk in bulks:
    weight = bulk[0][0] - bulk[1][0]
    tall = bulk[0][1] - bulk[1][1]
    if weight < 0 and tall < 0:
        bulk_dict[bulk[0][2]] += 1
    elif weight > 0 and tall > 0:
        bulk_dict[bulk[1][2]] += 1
temp_str = ''
for key,value in bulk_dict.items():
    value += 1
    temp_str += str(value) + ' '

print(temp_str[:-1])