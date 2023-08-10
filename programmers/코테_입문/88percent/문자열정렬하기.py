def solution(my_string):
    answer = []

    for i in my_string:
        try:
            answer.append(int(i))
        except:
            pass

    answer.sort()

    return answer



print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))