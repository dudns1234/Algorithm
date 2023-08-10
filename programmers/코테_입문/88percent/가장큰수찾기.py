def solution(array):
    answer = []

    answer.append()
    answer.append(array.index(max(array)))

    return answer

# 다른 풀이
def solution(array):
    return [max(array),array.index(max(array))]

print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))
