def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        time = 0
        fault = 0
        for s in skills:
            if s in skill:
                if s == skill[time]:
                    time += 1
                else:
                    fault = 1
                    break
        if fault == 0:
            answer += 1
    return answer

solution('CBD',["BACDE", "CBADF", "AECB", "BDA"])