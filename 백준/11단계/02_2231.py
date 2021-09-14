def find_under_num(devideme):
    for i in range(1, devideme):
        devide_to_str = list(map(int, str(i)))
        compareme = sum(devide_to_str)
        if devideme == compareme + i:
            print(i)
            return
    print(0)


inp = int(input())
find_under_num(inp)
