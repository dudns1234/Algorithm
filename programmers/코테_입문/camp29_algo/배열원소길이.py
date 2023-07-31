def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer


print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))