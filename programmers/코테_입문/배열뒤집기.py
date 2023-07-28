def solution(num_list):
    answer = []
    for i in range(1,len(num_list)+1):
        answer.append(num_list[-i])
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))
