def solution(s):
    answer = 0
    a = -1
    temp = s.split(' ')
    for i in temp:
        a += 1
        try:
            if int(i):
                answer += int(i)
        except:
            answer -= int(temp[a-1])

    return answer


print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))
