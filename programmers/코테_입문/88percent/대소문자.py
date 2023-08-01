def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper() == True:
            answer += i.lower()
        elif i.islower() == True:
            answer += i.upper()
    return answer

print(solution("cccCCC"))
print(solution("abCdEfghIJ"))

# 다른 풀이
def solution(my_string):
    return my_string.swapcase()


def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer