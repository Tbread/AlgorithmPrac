def solution(record):
    uid_dict = {}
    chats = []
    result = []
    for i in range(len(record)):
        arr = record[i].split(' ')
        if arr[0] == 'Enter' or arr[0] == 'Change':
            uid_dict[arr[1]] = arr[2]
        if arr[0] == 'Enter':
            arr.pop()
        record[i] = arr
    for tp in record:
        if tp[0] != 'Change':
            chats.append(tp)
    for chat in chats:
        temp_str1 = uid_dict[chat[1]] + '님이 '
        temp_str2 = ''
        if chat[0] == 'Enter':
            temp_str2 = '들어왔습니다.'
        elif chat[0] == 'Leave':
            temp_str2 = '나갔습니다.'
        result.append(temp_str1+temp_str2)
    return result
