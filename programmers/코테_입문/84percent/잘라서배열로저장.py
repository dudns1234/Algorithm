def solution(my_str, n):
    answer = []
    
    while len(my_str):
        if len(my_str) >= n:
            temp = my_str[0:n]
            my_str = my_str.replace(temp,'',1)
            answer.append(temp)
        else:
            temp = my_str
            my_str = my_str.replace(temp,'')
            answer.append(temp)

    return answer

print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))
print(solution("1231231231", 3))

# 다른 사람 풀이

def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]