def solution(my_string, num1, num2):
    answer = []
    for i in range(len(my_string)):
        print(i)
        if i != num1 and i != num2:
            answer.append(my_string[i])

    answer.insert(num1,my_string[num2])
    answer.insert(num2,my_string[num1])

    return ''.join(answer)


print(solution("hello",1,2))
print(solution("I love you",3,6))


# 다른 풀이
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)

print(solution("hello",1,2))
print(solution("I love you",3,6))