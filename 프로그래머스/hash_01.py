def solution(participant, completion):
    answer = ''
    # dict_list = []
    # reverse_dict_list = []
    # retire = []
    # true_count = {}
    # for part in participant:
    #     dict_list.append({"participant": part})
    # for comp in completion:
    #     dict_list.append({"completion": comp})
    #     reverse_dict_list.append({comp: "completion"})
    part_name_count = same_name(participant)
    comp_name_count = same_name(completion)
    # for part in participant:
    #     for i in range(len(reverse_dict_list)):
    #         test = part in reverse_dict_list[i]
    #         if test is False:
    #             answer = part
    #         if test is True:
    #             del reverse_dict_list[i]
    #         print(test)
    key_list = part_name_count.keys()
    keys = []
    for item in key_list:
        keys.append(item)
    for i in range(len(part_name_count)):
        name = keys[i]
        # exist_test = name in comp_name_count
        # if exist_test is False:
        #     answer = name
        #     return answer
        comp_count = comp_name_count.get(name)
        part_count = part_name_count.get(name)
        if comp_count != part_count:
            answer = name
            return answer


def same_name(names):
    name_count={}
    for name in names:
        if name in name_count:
            name_count[name]+=1
        else:
            name_count[name]=1
    return name_count

print(solution(["leo", "kiki","leo"], ["leo","kiki"]))
