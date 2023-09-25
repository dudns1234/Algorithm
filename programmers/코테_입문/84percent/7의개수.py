def solution(array):
    answer = 0
    temp = ''.join(map(str,array))
    for i in temp:
        if int(i) == 7:
            answer += 1
    return answer


print(solution([7,77,17]))
print(solution([10,29]))

# 다른사람 풀이
def solution(array):
    return str(array).count('7')