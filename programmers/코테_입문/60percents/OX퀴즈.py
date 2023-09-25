def solution(quiz):
    answer = []

    a = 0
    for i in quiz:
        a = list(i.split(' '))
        if a[1] == '-':
            b = int(a[0]) - int(a[2])
            if b == int(a[-1]):
                answer.append("O")
            else:
                answer.append("X")
        elif a[1] == '+':
            b = int(a[0]) + int(a[2])
            if b == int(a[-1]):
                answer.append("O")
            else:
                answer.append("X")

    return answer
    
print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
