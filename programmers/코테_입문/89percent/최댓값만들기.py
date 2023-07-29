def solution(numbers):
    answers = 1
    numbers.sort()
    for i in numbers:
        if i == numbers[-1]:
            answers *= i
        elif i == numbers[-2]:
            answers *= i
    return answers

print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))

# 다른풀이
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
