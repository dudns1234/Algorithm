def solution(common):
    answer = 0

    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1] + (common[1] - common[0])
        return answer
    else:
        a = common[1] // common[0]
        answer = common[-1] * a
        return answer

    # d = common[1] - common[0]
    # answer = common[0] + len(common) * d
    # return answer


print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))

