def solution(my_string):
    answer = []
    for i in my_string:
        try:
            int(i)
        except:
            my_string = my_string.replace(i,' ')

    return sum(list(map(int,my_string.split())))


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))