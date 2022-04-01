import sys
a = int(input())

for i in range(a):
    sum = 0
    notdumb = 0
    scores = sys.stdin.readline().strip().split(' ')
    people = int(scores[0])
    for v in range(len(scores)):
        if v == 0:
            continue
        else:
            sum += int(scores[v])
    aver = sum/people

    for v in range(len(scores)):
        if v == 0:
            continue
        else:
            if int(scores[v]) > aver:
                notdumb += 1
    nd = float(notdumb)
    p = float(people)
    per = (nd/p)*100
    print('%.3f' % per+'%')
