def solution(age):
    answer = []
    
    #alph = ['a','b','c','d','e','f','g','h','i','j']

    from string import ascii_lowercase

    alph = list(ascii_lowercase)

    for i in range(10000):
        if i == age:
            for j in list(str(age)):
                answer.append(alph[int(j)])

    return ''.join(answer)


print(solution(23))
print(solution(51))
print(solution(100))


# 다른 풀이
def solution(age):
    age = str(age)
    age = age.replace("0", "a")
    age = age.replace("1", "b")
    age = age.replace("2", "c")
    age = age.replace("3", "d")
    age = age.replace("4", "e")
    age = age.replace("5", "f")
    age = age.replace("6", "g")
    age = age.replace("7", "h")
    age = age.replace("8", "i")
    age = age.replace("9", "j")
    return age