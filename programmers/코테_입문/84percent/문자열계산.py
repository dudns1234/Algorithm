def solution(my_string):
    answer = 0
    my_string = my_string.split(' ')
    print(my_string)
    for i in range(1,len(my_string),2):
        if i == 1:
            if my_string[i] == "+":
                answer += int(my_string[i-1]) + int(my_string[i+1])
            else:
                answer += int(my_string[i-1]) - int(my_string[i+1])
        else:
            if my_string[i] == "+":
                answer +=  int(my_string[i+1])
            else:
                answer -= int(my_string[i+1])

    return answer

print(solution("3 + 4"))
print(solution("10 + 1"))
print(solution("3 + 4 - 5"))
