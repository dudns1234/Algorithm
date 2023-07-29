def solution(num_list):
    answer = []
    count1 = 0
    count2 = 0
    for i in num_list:
        if i % 2 == 0:
            count1 += 1
        else:
            count2 += 1
    answer.append(count1)
    answer.append(count2)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))


# 다른 풀이
def solution(num_list):
    answer = [0,0]

    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer