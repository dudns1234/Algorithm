def solution(my_string):
    answer = ''
    for i in range(1,len(my_string)+1):
        answer += my_string[-i]
    return answer

print(solution("jaron"))
print(solution("bread"))

# 다른 방법
def solution(my_string):
    answer = my_string.reverse()
    return answer

print(solution("jaron"))
print(solution("bread"))