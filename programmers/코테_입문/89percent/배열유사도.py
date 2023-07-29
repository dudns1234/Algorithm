def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
        else:
            continue
    return answer

print(solution(["a", "b", "c"],["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"],["m", "dot"]))

# 다른 풀이
def solution(s1, s2):
    return len(set(s1)&set(s2))