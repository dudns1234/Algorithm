def solution(emergency):
    answer = []

    temp = list(map(str,emergency))  # 기존 순서
    emergency.sort(reverse = True)
    temp2 = list(map(str,emergency))  # 내림차순
    a = 0
    for i in temp2:
        a += 1
        temp[temp.index(i)] = a

    return temp

print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))
