def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer += int(i)
        except:
            pass
    return answer
print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))