def solution(numbers, k):
    answer = 0

    i = 0
    count = 0
    while True:
        
        if len(numbers) == i:
            i = 0
            answer = numbers[i]
            count += 1
            i += 2
        elif len(numbers) < i:
            i = 1
            answer = numbers[i]
            count += 1
            i += 2
        else:
            answer = numbers[i]
            count += 1
            i += 2

        if count == k:
            break

    return answer



print(solution([1, 2, 3, 4],2))
print(solution([1, 2, 3, 4, 5, 6],5))
print(solution([1, 2, 3],3))

# number[0] -> number[2]

# number[0] -> number[2] -> number[4]-> number[6]  : len(6)
# number[0] -> number[2] -> number[4]-> number[0] -> number[2]


# number[0] -> number[2] -> number[4]-> number[6]-> number[8]  :len(6)
# number[0] -> number[2] -> number[4]-> number[6] -> number[1]

# number[0]-> number[2] -> number[4] len(3)
# number[0]-> number[2] -> number[1]