def solution(array, height):
    answer = 0
    for i in array:
        if i > height :
            answer += 1
        else:
            answer += 0 # continue 로만 써도 가능
    return answer

print(solution([149, 180, 192, 170],167))
print(solution([180, 120, 140],190))

# 다른풀이

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)