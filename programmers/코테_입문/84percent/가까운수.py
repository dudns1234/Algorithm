def solution(array, n):
    answer = 100000000
    result = 0
    for i in array:
        if answer > abs(i-n):
            answer = abs(i-n)
            result = i
        elif answer == abs(i-n):
            if result > i:
                result = i

    return result


print(solution([3, 10, 28],20))
print(solution([10, 11, 12],13))

