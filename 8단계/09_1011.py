import sys

a = int(input())
for repeat in range(a):
    l = (sys.stdin.readline().strip()).split(' ')
    goal = int(l[1]) - int(l[0])
    speed = 1
    remaindistance = goal
    calc = 0
    movedistance = 0
    i = 0
    chkd = 0
    whentwice = 0
    while(chkd < remaindistance):
        i += 1
        movedistance += speed
        remaindistance = goal - movedistance
        for m in range(1,speed+1):
            calc += m
        if remaindistance <= calc:
            calc -= speed
            whentwice = remaindistance - calc
            speed -= 1
            print(speed)
        else:
            speed += 1
            print(speed)
