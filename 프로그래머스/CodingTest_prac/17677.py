import re
global word_dict
def solution(str1, str2):
    word_dict = {}
    str1_arr = split_str(str1,1)
    str2_arr = split_str(str2,2)






def split_str(s,num):
    arr = []
    s = s.lower()
    for i in range(len(s)-1):
        temp_str = s[i:i+2]
        if re.search('[^a-zA-Z]',temp_str):
            continue
        arr.append(temp_str)
        if word_dict[temp_str]:
            if word_dict[temp_str] == num:
                init_num = 0
                while True:
                    init_num += 1
                    if word_dict[temp_str+str(init_num)]:
                        if word_dict[temp_str+str(init_num)] == num:
                            continue
                        else:
                            word_dict[temp_str+str(init_num)] = num
                            break
                    else:
                        word_dict[temp_str+str(init_num)] = num
                        break
            else:
                word_dict[temp_str] = num
        else:
            word_dict[temp_str]


        else:
            word_dict[temp_str] = 1
    return arr

solution('FRANCE','french')