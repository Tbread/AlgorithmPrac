import sys
inp = list(sys.stdin.readline().split())
inp = sorted(list(inp[0]),reverse=True)
str = ''
for i in inp:
    str += i
print(str)