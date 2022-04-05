from math import ceil
def solution(n, words):
    word_dict = {}
    foul = False
    temp = '0'
    for i in range(len(words)):
        if temp[-1] != words[i][0] and i != 0:
            foul = True
            turn = i
            break
        if words[i] in word_dict:
            foul = True
            turn = i
            break
        else:
            word_dict[words[i]] = 1
            temp = words[i]
    if foul:
        fouler = (i+1) % n
        if fouler == 0:
            fouler = n
        return [fouler,ceil((i+1)/n)]
    return [0, 0]


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))