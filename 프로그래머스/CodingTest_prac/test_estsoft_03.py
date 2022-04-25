def solution(record):
    records = []
    room = []
    for rec in record:
        temp = rec.replace('id=', '').replace('k=', '').split()
        temp[0] = int(temp[0])
        if len(temp) == 3:
            temp[2] = int(temp[2])
        records.append(temp)
    sit = 0
    for rec in records:
        if rec[1] == 'leave':
            for i in range(len(room)):
                if room[i][1] == rec[0]:
                    space = room[i - 1][0] + room[i + 1][0] + 1
                    del room[i + 1]
                    room[i - 1][0] = space
                    del room[i]
                    break
        if sit == 0:
            room.append([rec[2], 0])
            room.append([1, rec[0], rec[2]])
            room.append([rec[2], 0])
            sit += 1
            continue
        if sit == 1 and rec[1] == 'sit' and len(room) == 3:
            need = room[1][2]
            if need >= rec[2]:
                room.append([1, rec[0], rec[2]])
                room.append([rec[2], 0])
            else:
                room[-1][0] = rec[2]
                room.append([1, rec[0], rec[2]])
                room.append([rec[2], 0])
            sit += 1
            continue
        if sit == 1 and rec[1] == 'sit' and len(room) == 1:
            room = [[rec[2], 0], [1, rec[0], rec[2]], [rec[2], 0]]
            sit += 1
            continue
        if rec[1] == 'sit':
            flag = 0
            for i in range(len(room)-1):
                if room[i][0] >= (rec[2] * 2 + 1):
                    if i == 0:
                        if rec[2] >= room[i+1][2]:
                            temp = rec[2]
                        else:
                            temp = room[i+1][2]
                        if not room[i][0] >= 1 + temp + rec[2]:
                            continue
                        room.insert(0,[rec[2],0])
                        room.insert(1,[1,rec[0],rec[2]])
                        room[2][0] = room[2][0] - 1 - rec[2]
                        break
                    if rec[2] >= room[i - 1][2]:
                        temp1 = rec[2]
                    else:
                        temp1 = room[i - 1][2]
                    if rec[2] >= room[i + 1][2]:
                        temp2 = rec[2]
                    else:
                        temp2 = room[i + 1][2]
                    if temp1 + temp2 + 1 <= room[i][0]:
                        room.insert(i + 1, [1, rec[0]])
                        room.insert(i + 2, [room[i][0] - temp1 - 1, 0])
                        room[i][0] = temp1
                        flag = 1
                        break
            if flag == 0:
                if rec[2] >= room[-1][0]:
                    room[-1][0] = rec[2]
                    room.append([1,rec[0],rec[2]])
                    room.append([rec[2],0])
                else:
                    room.append([1,rec[0],rec[2]])
                    room.append([rec[2],0])
    position = 0
    answer = []
    for i in range(len(room)):
        if room[i][1] == 0:
            position += room[i][0]
        else:
            answer.append([room[i][1],position])
            position += 1
    answer.sort(key=lambda x:x[0])
    print(answer)
    print(room)
    return answer


solution(["id=1 sit k=1","id=2 sit k=3","id=1 leave","id=3 sit k=1"])
