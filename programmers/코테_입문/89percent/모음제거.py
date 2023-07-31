def solution(my_string):
    answer = ''
    remove = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in remove:
            answer += i
    return answer

# 다른풀이
def solution(my_string):
    remove = ['a','e','i','o','u']
    for i in remove:
        my_string = my_string.replace(i, '')
    return my_string

print(solution("bus"))
print(solution("nice to meet you"))