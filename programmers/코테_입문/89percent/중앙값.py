def solution(array):
    answer = 0
    array.sort()
    i = (len(array)//2)
    answer = array[i]

    return answer

print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))


# 다른 풀이
def solution(array):
    array = sorted(array)
    return array[len(array)//2]