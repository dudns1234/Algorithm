def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer


print(solution("2"))
print(solution("205"))

# 가위 = 2 / 0
# 바위 = 0 / 5
# 보 = 5 / 2