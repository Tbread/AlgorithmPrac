def solution(commands):
    answer = []
    cell = [["EMPTY"] * 50 for _ in range(50)]
    merge_dict = {[1, 1]: [2, 3]}
    value_dict = {}
    for command in commands:
        top_Command = command.split()[0]
        if top_Command == "UPDATE":
            if len(command.split()) == 4:
                y, x, value = int(command.split()[1]) - 1, int(command.split()[2]) - 1, command.split()[3]
                cell[y][x] = value
                if value in value_dict:
                    value_dict[value].append([y, x])
                else:
                    value_dict[value] = [[y, x]]
                if [y, x] in merge_dict:
                    cell[merge_dict[y, x][0]][merge_dict[y, x][1]] = value
            elif len(command.split()) == 3:
                old_value, new_value = command.split()[1], command.split()[2]

        #
        # elif top_Command == "MERGE":
        # elif top_Command == "UNMERGE":
        # elif top_Command == "PRINT":


solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice",
          "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta",
          "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik",
          "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
