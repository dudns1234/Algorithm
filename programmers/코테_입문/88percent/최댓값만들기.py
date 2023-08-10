def solution(numbers):
    answer = []

    for a in range(len(numbers)):
        for b in range(len(numbers)):
            if a == b:
                pass
            else:
                answer.append(numbers[a]*numbers[b])

    return max(answer)

print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))
