def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))